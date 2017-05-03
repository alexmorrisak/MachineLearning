# fc_pcb_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def hf(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'is_hf', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('pcb', 'needs_hf_mat',
                       (rule.pattern(0).as_data(context),)),
        engine.assert_('pcb', 'needs_ctrl_z',
                       (rule.pattern(0).as_data(context),)),
        engine.assert_('pcb', 'needs_gnd_layer',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def needs_no_hf(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'is_not_hf', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('pcb', 'needs_no_hf_mat',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def large_budget_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'is_short_timeline', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('pcb', 'needs_large_budget',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def large_budget_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'is_critical', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('pcb', 'needs_large_budget',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def recommend__material_1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'needs_hf_mat', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('pcb', 'needs_large_budget', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('pcb', 'is_hf_mat', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('pcb', 'is_expensive_mat', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    engine.assert_('pcb', 'good_material',
                                   (rule.pattern(0).as_data(context),
                                    rule.pattern(1).as_data(context),)),
                    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def recommend__material_2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'needs_hf_mat', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('pcb', 'is_hf_mat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('pcb', 'good_material',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def recommend__material_3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'needs_no_hf_mat', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('pcb', 'is_not_hf_mat', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('pcb', 'good_material',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def gnd_separation(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pcb', 'requires_isolation', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('net1') != context.lookup_data('net2'):
          engine.assert_('pcb', 'needs_gnd_layer',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_pcb')
  
  fc_rule.fc_rule('hf', This_rule_base, hf,
    (('pcb', 'is_hf',
      (contexts.variable('net'),),
      False),),
    (contexts.variable('net'),))
  
  fc_rule.fc_rule('needs_no_hf', This_rule_base, needs_no_hf,
    (('pcb', 'is_not_hf',
      (contexts.variable('net'),),
      False),),
    (contexts.variable('net'),))
  
  fc_rule.fc_rule('large_budget_1', This_rule_base, large_budget_1,
    (('pcb', 'is_short_timeline',
      (contexts.variable('circuit'),),
      False),),
    (contexts.variable('circuit'),))
  
  fc_rule.fc_rule('large_budget_2', This_rule_base, large_budget_2,
    (('pcb', 'is_critical',
      (contexts.variable('circuit'),),
      False),),
    (contexts.variable('circuit'),))
  
  fc_rule.fc_rule('recommend__material_1', This_rule_base, recommend__material_1,
    (('pcb', 'needs_hf_mat',
      (contexts.variable('net'),),
      False),
     ('pcb', 'needs_large_budget',
      (contexts.variable('circuit'),),
      False),
     ('pcb', 'is_hf_mat',
      (contexts.variable('material'),),
      False),
     ('pcb', 'is_expensive_mat',
      (contexts.variable('material'),),
      False),),
    (contexts.variable('net'),
     contexts.variable('material'),))
  
  fc_rule.fc_rule('recommend__material_2', This_rule_base, recommend__material_2,
    (('pcb', 'needs_hf_mat',
      (contexts.variable('net'),),
      False),
     ('pcb', 'is_hf_mat',
      (contexts.variable('material'),),
      False),),
    (contexts.variable('net'),
     contexts.variable('material'),))
  
  fc_rule.fc_rule('recommend__material_3', This_rule_base, recommend__material_3,
    (('pcb', 'needs_no_hf_mat',
      (contexts.variable('net'),),
      False),
     ('pcb', 'is_not_hf_mat',
      (contexts.variable('material'),),
      False),),
    (contexts.variable('net'),
     contexts.variable('material'),))
  
  fc_rule.fc_rule('gnd_separation', This_rule_base, gnd_separation,
    (('pcb', 'requires_isolation',
      (contexts.variable('net1'),
       contexts.variable('net2'),),
      False),),
    (contexts.variable('net1'),))


Krb_filename = '../fc_pcb.krb'
Krb_lineno_map = (
    ((13, 17), (27, 27)),
    ((18, 19), (29, 29)),
    ((20, 21), (30, 30)),
    ((22, 23), (31, 31)),
    ((32, 36), (36, 36)),
    ((37, 38), (38, 38)),
    ((47, 51), (43, 43)),
    ((52, 53), (45, 45)),
    ((62, 66), (50, 50)),
    ((67, 68), (52, 52)),
    ((77, 81), (57, 57)),
    ((82, 86), (58, 58)),
    ((87, 91), (59, 59)),
    ((92, 96), (60, 60)),
    ((97, 99), (62, 62)),
    ((108, 112), (67, 67)),
    ((113, 117), (68, 68)),
    ((118, 120), (70, 70)),
    ((129, 133), (75, 75)),
    ((134, 138), (76, 76)),
    ((139, 141), (78, 78)),
    ((150, 154), (83, 83)),
    ((155, 155), (84, 84)),
    ((156, 157), (86, 86)),
)
