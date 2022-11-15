''' This is a folder for migration

Add each migration as a file like: yyy-mm-dd-HHmm-name.py
they get ordered when they're run:

the script is like:
from ._migration import migrate

@migrate('dd-mm-hh-mm-HHMM', 'name')
def name(store):
    # do stuff

All files NOT prefixed with _ will be imported and thus added for migration.
'''

from importlib import import_module
from pathlib import Path

for f in Path(__file__).parent.glob("*.py"):
    module_name = f.stem
    if (not module_name.startswith("_")) and (module_name not in globals()):
        import_module(f".{module_name}", __package__)
    del f, module_name

del import_module, Path
