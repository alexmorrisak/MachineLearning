# $Id: driver.py 6de8ee4e7d2d 2010-03-29 mtnyogi $
# coding=utf-8
# 
# Copyright © 2007-2008 Bruce Frederiksen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

'''
    This example shows how people are related.  The primary data (facts) that
    are used to figure everything out are in family.kfb.

    There are four independent rule bases that all do the same thing.  The
    fc_example rule base only uses forward-chaining rules.  The bc_example
    rule base only uses backward-chaining rules.  The bc2_example rule base
    also only uses backward-chaining rules, but with a few optimizations that
    make it run 100 times faster than bc_example.  And the example rule base
    uses all three (though it's a poor use of plans).

    Once the pyke engine is created, all the rule bases loaded and all the
    primary data established as universal facts; there are five functions
    that can be used to run each of the three rule bases: fc_test, bc_test,
    bc2_test, test and general.
'''

from __future__ import with_statement
import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback, goal

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

#fc_goal = goal.compile('family.how_related($person1, $person2, $relationship)')
#fc_goal = goal.compile('pcb.is_expensive_mat($material)')

def recommend_materials():
    fc_goal = goal.compile('pcb.good_material($net, $material)')
    engine.reset()      # Allows us to run tests multiple times.

    # Also runs all applicable forward-chaining rules.
    start_time = time.time()
    engine.activate('fc_pcb')
    #print "dumping facts..:"
    #engine.get_kb('pcb').dump_universal_facts()
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "Recommended material options:"
    try:
        # In this case, the relationship is returned when you run the plan.
        with fc_goal.prove(
               engine\
               ) \
          as gen:
            for vars, plan in gen:
                print "%s: %s" % (vars['net'], vars['material'])
                #print "%s is a suitable material for %s" % (vars['material'], vars['net'])
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    #engine.print_stats()
    #print "fc time %.2f, %.0f asserts/sec" % \
    #      (fc_time, engine.get_kb('pcb').get_stats()[2] / fc_time)
    #print "bc time %.2f, %.0f goals/sec" % \
    #      (prove_time, engine.get_kb('example').num_prove_calls / prove_time)
    #print "total time %.2f" % (fc_time + prove_time)

def create_stackup():
    fc_goal = goal.compile('pcb.needs_gnd_layer($net)')
    engine.reset()      # Allows us to run tests multiple times.

    # Also runs all applicable forward-chaining rules.
    start_time = time.time()
    engine.activate('fc_pcb')
    #print "dumping facts..:"
    #engine.get_kb('pcb').dump_universal_facts()
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "Requires neighboring gnd layer:"
    try:
        # In this case, the relationship is returned when you run the plan.
        with fc_goal.prove(
               engine\
               ) \
          as gen:
            for vars, plan in gen:
                print "%s" % (vars['net'])
                #print "%s is a suitable material for %s" % (vars['material'], vars['net'])
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

def recommend_controlled_z():
    fc_goal = goal.compile('pcb.needs_ctrl_z($net)')
    engine.reset()      # Allows us to run tests multiple times.

    # Runs all applicable forward-chaining rules.
    engine.activate('fc_pcb')
    print "Requires controlled impedance tracewidth:"
    try:
        # In this case, the relationship is returned when you run the plan.
        with fc_goal.prove(
               engine\
               ) \
          as gen:
            for vars, plan in gen:
                print "%s" % (vars['net'])
                #print "%s is a suitable material for %s" % (vars['material'], vars['net'])
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

def do_all():
    engine.add_universal_fact('pcb', 'is_hf',  ('net1',))
    engine.add_universal_fact('pcb', 'is_hf',  ('net4',))


    print '******************'
    create_stackup()
    print '******************'
    recommend_controlled_z()
    print '******************'
    recommend_materials()
    print '******************'
    #prove_time = time.time() - fc_end_time
    #print
    #print "done"
    engine.print_stats()
    #print "fc time %.2f, %.0f asserts/sec" % \
    #      (fc_time, engine.get_kb('pcb').get_stats()[2] / fc_time)
    ##print "bc time %.2f, %.0f goals/sec" % \
    ##      (prove_time, engine.get_kb('example').num_prove_calls / prove_time)
    #print "total time %.2f" % (fc_time + prove_time)

