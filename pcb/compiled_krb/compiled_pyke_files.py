# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'example.krb'):
           [1492861852.38885, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'pcb.kfb'):
           [1493204790.709206, 'pcb.fbc'],
         ('', '', 'bc2_example.krb'):
           [1492861852.609849, 'bc2_example_bc.py'],
         ('', '', 'bc_example.krb'):
           [1492861852.76698, 'bc_example_bc.py'],
         ('', '', 'fc_example.krb'):
           [1492861852.900698, 'fc_example_fc.py'],
         ('', '', 'fc_pcb.krb'):
           [1492908752.661457, 'fc_pcb_fc.py'],
        },
        compiler_version)

