# fc_example_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def needs_hifreq(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('circuit', 'is_hf', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('circuit', 'needs_hf',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def son_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def daughter_of(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(4).as_data(context),
                        rule.pattern(5).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brothers(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'son_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('brother1') != context.lookup_data('brother2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def sisters(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'daughter_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('sister1') != context.lookup_data('sister2'):
              engine.assert_('family', 'siblings',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),
                              rule.pattern(2).as_data(context),
                              rule.pattern(2).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def brother_and_sister(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'son_of', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'daughter_of', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'siblings',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),)),
            engine.assert_('family', 'siblings',
                           (rule.pattern(1).as_data(context),
                            rule.pattern(0).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(2).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def facts_for_bc_rules(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    engine.assert_('family', 'as_au',
                   (rule.pattern(0).as_data(context),
                    rule.pattern(1).as_data(context),)),
    engine.assert_('family', 'as_au',
                   (rule.pattern(2).as_data(context),
                    rule.pattern(3).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(4).as_data(context),
                    rule.pattern(5).as_data(context),)),
    engine.assert_('family', 'as_nn',
                   (rule.pattern(6).as_data(context),
                    rule.pattern(7).as_data(context),)),
    rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def niece_or_nephew_and_aunt_or_uncle(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'siblings', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'as_au', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                with knowledge_base.Gen_once if index == 3 \
                         else engine.lookup('family', 'as_nn', context,
                                            rule.foreach_patterns(3)) \
                  as gen_3:
                  for dummy in gen_3:
                    mark4 = context.mark(True)
                    if rule.pattern(0).match_data(context, context,
                            ('great',) * len(context.lookup_data('depth'))):
                      context.end_save_all_undo()
                      engine.assert_('family', 'nn_au',
                                     (rule.pattern(1).as_data(context),
                                      rule.pattern(2).as_data(context),
                                      rule.pattern(0).as_data(context),
                                      rule.pattern(3).as_data(context),
                                      rule.pattern(4).as_data(context),)),
                      rule.rule_base.num_fc_rules_triggered += 1
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
  finally:
    context.done()

def parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'child_parent',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),
                        rule.pattern(4).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def grand_parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'child_parent',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(4).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def great_grand_parent_and_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            engine.assert_('family', 'child_parent',
                           (rule.pattern(0).as_data(context),
                            rule.pattern(1).as_data(context),
                            rule.pattern(2).as_data(context),
                            rule.pattern(3).as_data(context),
                            rule.pattern(4).as_data(context),)),
            rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def first_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'siblings', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'child_parent', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                engine.assert_('family', 'cousins',
                               (rule.pattern(0).as_data(context),
                                rule.pattern(1).as_data(context),
                                rule.pattern(2).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def nth_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'cousins', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            with knowledge_base.Gen_once if index == 2 \
                     else engine.lookup('family', 'child_parent', context,
                                        rule.foreach_patterns(2)) \
              as gen_2:
              for dummy in gen_2:
                mark3 = context.mark(True)
                if rule.pattern(0).match_data(context, context,
                        context.lookup_data('n') + 1):
                  context.end_save_all_undo()
                  engine.assert_('family', 'cousins',
                                 (rule.pattern(1).as_data(context),
                                  rule.pattern(2).as_data(context),
                                  rule.pattern(0).as_data(context),)),
                  rule.rule_base.num_fc_rules_triggered += 1
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
  finally:
    context.done()

def how_related_child_parent(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_parent_child(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_siblings(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'siblings', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('family', 'how_related',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def how_related_nn_au(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'nn_au', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_au_nn(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'nn_au', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                add_prefix(context.lookup_data('prefix'), context.lookup_data('p1_type'), context.lookup_data('p2_type'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'cousins', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                nth(context.lookup_data('n'))):
          context.end_save_all_undo()
          engine.assert_('family', 'how_related',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),
                          rule.pattern(3).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
  finally:
    context.done()

def how_related_removed_cousins(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'child_parent', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'cousins', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            mark2 = context.mark(True)
            if rule.pattern(0).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      len(context.lookup_data('grand')) + 1):
                context.end_save_all_undo()
                engine.assert_('family', 'how_related',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
  finally:
    context.done()

def how_related_cousins_removed(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('family', 'cousins', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('family', 'child_parent', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            mark2 = context.mark(True)
            if rule.pattern(0).match_data(context, context,
                    nth(context.lookup_data('n'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(1).match_data(context, context,
                      len(context.lookup_data('grand')) + 1):
                context.end_save_all_undo()
                engine.assert_('family', 'how_related',
                               (rule.pattern(2).as_data(context),
                                rule.pattern(3).as_data(context),
                                rule.pattern(4).as_data(context),)),
                rule.rule_base.num_fc_rules_triggered += 1
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('fc_example')
  
  fc_rule.fc_rule('needs_hifreq', This_rule_base, needs_hifreq,
    (('circuit', 'is_hf',
      (contexts.variable('circuit'),),
      False),),
    (contexts.variable('circuit'),))
  
  fc_rule.fc_rule('son_of', This_rule_base, son_of,
    (('family', 'son_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('son'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('daughter_of', This_rule_base, daughter_of,
    (('family', 'daughter_of',
      (contexts.variable('child'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('father'),
     pattern.pattern_literal('father'),
     pattern.pattern_literal('daughter'),
     contexts.variable('mother'),
     pattern.pattern_literal('mother'),))
  
  fc_rule.fc_rule('brothers', This_rule_base, brothers,
    (('family', 'son_of',
      (contexts.variable('brother1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'son_of',
      (contexts.variable('brother2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother1'),
     contexts.variable('brother2'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('sisters', This_rule_base, sisters,
    (('family', 'daughter_of',
      (contexts.variable('sister1'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister2'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('sister1'),
     contexts.variable('sister2'),
     pattern.pattern_literal('sister'),))
  
  fc_rule.fc_rule('brother_and_sister', This_rule_base, brother_and_sister,
    (('family', 'son_of',
      (contexts.variable('brother'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),
     ('family', 'daughter_of',
      (contexts.variable('sister'),
       contexts.variable('father'),
       contexts.variable('mother'),),
      False),),
    (contexts.variable('brother'),
     contexts.variable('sister'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('brother'),))
  
  fc_rule.fc_rule('facts_for_bc_rules', This_rule_base, facts_for_bc_rules,
    (),
    (pattern.pattern_literal('brother'),
     pattern.pattern_literal('uncle'),
     pattern.pattern_literal('sister'),
     pattern.pattern_literal('aunt'),
     pattern.pattern_literal('son'),
     pattern.pattern_literal('nephew'),
     pattern.pattern_literal('daughter'),
     pattern.pattern_literal('niece'),))
  
  fc_rule.fc_rule('niece_or_nephew_and_aunt_or_uncle', This_rule_base, niece_or_nephew_and_aunt_or_uncle,
    (('family', 'child_parent',
      (contexts.variable('nn'),
       contexts.variable('parent'),
       contexts.variable('depth'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'siblings',
      (contexts.variable('parent'),
       contexts.variable('au'),
       contexts.variable('sibling_type'),
       contexts.anonymous('_'),),
      False),
     ('family', 'as_au',
      (contexts.variable('sibling_type'),
       contexts.variable('au_type'),),
      False),
     ('family', 'as_nn',
      (contexts.variable('child_type'),
       contexts.variable('nn_type'),),
      False),),
    (contexts.variable('greats'),
     contexts.variable('nn'),
     contexts.variable('au'),
     contexts.variable('au_type'),
     contexts.variable('nn_type'),))
  
  fc_rule.fc_rule('parent_and_child', This_rule_base, parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('parent'),
       contexts.variable('parent_type'),
       contexts.variable('child_type'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('parent'),
     pattern.pattern_literal(()),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('grand_parent_and_child', This_rule_base, grand_parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('parent'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('parent'),
       contexts.variable('grand_parent'),
       contexts.variable('parent_type'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('grand_parent'),
     pattern.pattern_literal(('grand',)),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('great_grand_parent_and_child', This_rule_base, great_grand_parent_and_child,
    (('family', 'child_parent',
      (contexts.variable('child'),
       contexts.variable('grand_child'),
       contexts.anonymous('_'),
       contexts.variable('child_type'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('grand_child'),
       contexts.variable('grand_parent'),
       pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
       contexts.variable('parent_type'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('child'),
     contexts.variable('grand_parent'),
     pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
     contexts.variable('parent_type'),
     contexts.variable('child_type'),))
  
  fc_rule.fc_rule('first_cousins', This_rule_base, first_cousins,
    (('family', 'child_parent',
      (contexts.variable('cousin1'),
       contexts.variable('sibling1'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'siblings',
      (contexts.variable('sibling1'),
       contexts.variable('sibling2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('cousin2'),
       contexts.variable('sibling2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_literal(1),))
  
  fc_rule.fc_rule('nth_cousins', This_rule_base, nth_cousins,
    (('family', 'child_parent',
      (contexts.variable('next_cousin1'),
       contexts.variable('cousin1'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('next_cousin2'),
       contexts.variable('cousin2'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('next_n'),
     contexts.variable('next_cousin1'),
     contexts.variable('next_cousin2'),))
  
  fc_rule.fc_rule('how_related_child_parent', This_rule_base, how_related_child_parent,
    (('family', 'child_parent',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('prefix'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_parent_child', This_rule_base, how_related_parent_child,
    (('family', 'child_parent',
      (contexts.variable('person2'),
       contexts.variable('person1'),
       contexts.variable('prefix'),
       contexts.variable('p1_type'),
       contexts.variable('p2_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_siblings', This_rule_base, how_related_siblings,
    (('family', 'siblings',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('person1'),
     contexts.variable('person2'),
     pattern.pattern_tuple((contexts.variable('p1_type'), contexts.variable('p2_type'),), None),))
  
  fc_rule.fc_rule('how_related_nn_au', This_rule_base, how_related_nn_au,
    (('family', 'nn_au',
      (contexts.variable('person1'),
       contexts.variable('person2'),
       contexts.variable('prefix'),
       contexts.variable('p2_type'),
       contexts.variable('p1_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_au_nn', This_rule_base, how_related_au_nn,
    (('family', 'nn_au',
      (contexts.variable('person2'),
       contexts.variable('person1'),
       contexts.variable('prefix'),
       contexts.variable('p1_type'),
       contexts.variable('p2_type'),),
      False),),
    (contexts.variable('relationship'),
     contexts.variable('person1'),
     contexts.variable('person2'),))
  
  fc_rule.fc_rule('how_related_cousins', This_rule_base, how_related_cousins,
    (('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'),), None),))
  
  fc_rule.fc_rule('how_related_removed_cousins', This_rule_base, how_related_removed_cousins,
    (('family', 'child_parent',
      (contexts.variable('removed_cousin1'),
       contexts.variable('cousin1'),
       contexts.variable('grand'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),
     ('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('r1'),
     contexts.variable('removed_cousin1'),
     contexts.variable('cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),))
  
  fc_rule.fc_rule('how_related_cousins_removed', This_rule_base, how_related_cousins_removed,
    (('family', 'cousins',
      (contexts.variable('cousin1'),
       contexts.variable('cousin2'),
       contexts.variable('n'),),
      False),
     ('family', 'child_parent',
      (contexts.variable('removed_cousin2'),
       contexts.variable('cousin2'),
       contexts.variable('grand'),
       contexts.anonymous('_'),
       contexts.anonymous('_'),),
      False),),
    (contexts.variable('nth'),
     contexts.variable('r1'),
     contexts.variable('cousin1'),
     contexts.variable('removed_cousin2'),
     pattern.pattern_tuple((contexts.variable('nth'), pattern.pattern_literal('cousins'), contexts.variable('r1'), pattern.pattern_literal('removed'),), None),))

def nth(n):
    if n % 10 not in (1, 2, 3) or 10 < n % 100 < 20: return "%dth" % n
    if n % 10 == 1: return "%dst" % n
    if n % 10 == 2: return "%dnd" % n
    if n % 10 == 3: return "%drd" % n
def add_prefix(prefix, x, y):
    if not prefix: return (x, y)
    return (prefix + (x,), prefix + (y,))

Krb_filename = '../fc_example.krb'
Krb_lineno_map = (
    ((13, 17), (26, 26)),
    ((18, 19), (28, 28)),
    ((28, 32), (39, 39)),
    ((33, 37), (41, 41)),
    ((38, 42), (42, 42)),
    ((51, 55), (46, 46)),
    ((56, 60), (48, 48)),
    ((61, 65), (49, 49)),
    ((74, 78), (54, 54)),
    ((79, 83), (55, 55)),
    ((84, 84), (56, 56)),
    ((85, 89), (58, 58)),
    ((98, 102), (62, 62)),
    ((103, 107), (63, 63)),
    ((108, 108), (64, 64)),
    ((109, 113), (66, 66)),
    ((122, 126), (70, 70)),
    ((127, 131), (71, 71)),
    ((132, 136), (73, 73)),
    ((137, 141), (74, 74)),
    ((150, 152), (84, 84)),
    ((153, 155), (85, 85)),
    ((156, 158), (86, 86)),
    ((159, 161), (87, 87)),
    ((170, 174), (91, 91)),
    ((175, 179), (92, 92)),
    ((180, 184), (93, 93)),
    ((185, 189), (94, 94)),
    ((192, 192), (95, 95)),
    ((194, 199), (97, 97)),
    ((210, 214), (103, 103)),
    ((215, 220), (105, 105)),
    ((229, 233), (109, 109)),
    ((234, 238), (110, 110)),
    ((239, 244), (114, 115)),
    ((253, 257), (119, 119)),
    ((258, 262), (121, 122)),
    ((263, 268), (124, 125)),
    ((277, 281), (129, 129)),
    ((282, 286), (130, 130)),
    ((287, 291), (131, 131)),
    ((292, 295), (133, 133)),
    ((304, 308), (137, 137)),
    ((309, 313), (138, 138)),
    ((314, 318), (139, 139)),
    ((321, 321), (140, 140)),
    ((323, 326), (142, 142)),
    ((337, 341), (146, 146)),
    ((344, 344), (147, 147)),
    ((346, 349), (149, 149)),
    ((360, 364), (165, 165)),
    ((367, 367), (166, 166)),
    ((369, 372), (168, 168)),
    ((383, 387), (172, 172)),
    ((388, 391), (174, 174)),
    ((400, 404), (178, 178)),
    ((407, 407), (179, 179)),
    ((409, 412), (181, 181)),
    ((423, 427), (188, 188)),
    ((430, 430), (189, 189)),
    ((432, 435), (191, 191)),
    ((446, 450), (195, 195)),
    ((453, 453), (196, 196)),
    ((455, 458), (198, 198)),
    ((469, 473), (202, 202)),
    ((474, 478), (203, 203)),
    ((481, 481), (204, 204)),
    ((485, 485), (205, 205)),
    ((487, 490), (207, 208)),
    ((503, 507), (212, 212)),
    ((508, 512), (213, 213)),
    ((515, 515), (214, 214)),
    ((519, 519), (215, 215)),
    ((521, 524), (217, 218)),
)
