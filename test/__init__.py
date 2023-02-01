''' This is a folder for migration

Add each migration as a file like: yyy-mm-dd-HHmm-name.py
they get ordered when they're run:

the script is like:
from ._test import test

@test('dd-mm-hh-mm-HHMM', 'name')
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

from ._test import test_funcs
def run_tests(verbose, test_name):
    results = []
    total = {
        "tests":0,
        "passed":0,
        "finished":0,
        "clean":0,
        "elapsed": 0,
    }
    for test in test_funcs:
        r=test(test_name)
        if r is None:
            continue
        if verbose:
            print(r['test'],'-', 'passed' if r['passed'] else 'FAILED')
        results.append(r)
        total["tests"]+=1
        for metric in ["passed","finished","clean"]:
            if r[metric]:
                total[metric]+=1
        total["elapsed"]+=r["elapsed"]
    total["results"]=results
    return total
