# pcb_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def needs_hifreq(rule, context = None, index = None):
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
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('pcb')
  
  fc_rule.fc_rule('needs_hifreq', This_rule_base, needs_hifreq,
    (('pcb', 'is_hf',
      (contexts.variable('circuit'),),
      False),),
    (contexts.variable('circuit'),))


Krb_filename = '../pcb.krb'
Krb_lineno_map = (
    ((13, 17), (26, 26)),
    ((18, 19), (28, 28)),
)
