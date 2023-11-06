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

# useful!
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def highlight(text, style):
        return style+text+bcolors.ENDC

from ._test import test_funcs
def run_tests(verbose, loud, exceptions, test_list, file_list, pp):
    results = []
    total = {
        "tests":0,
        "passed":0,
        "finished":0,
        "clean":0,
        "elapsed": 0,
        "test_exception": 0,
        "scaffold_exception": 0,
    }

    current_file = None
    def check_file(previous, result):
        current = result['file']
        if previous == current:
            return previous
        print(bcolors.highlight(f"File: {current}.py", bcolors.HEADER+bcolors.UNDERLINE))
        return current

    for test in test_funcs:
        test_results=test(test_list, file_list)
        if test_results is None:
            continue
        current_file=check_file(current_file,test_results[0])
        for r in test_results:
            if r.get('test_exception'):
                ex = r.get('test_exception')
                if exceptions:
                    print(f"{type(ex).__name__} in test at line {ex.__traceback__.tb_lineno} of {__file__}: {ex}")
                r['test_exception'] = str(ex)
            
            if r.get('scaffold_exception'):
                ex = r.get('scaffold_exception')
                if exceptions:
                    print(f"{type(ex).__name__} in scaffold at line {ex.__traceback__.tb_lineno} of {__file__}: {ex}")
                r['scaffold_exception'] = str(ex)
                
            if loud and (not r['passed'] or not r['clean']) :
                pp.pprint(r)

            if verbose:
                if test_list is not None:
                    pp.pprint(r)
                if r['passed'] and r['clean']:
                    result = bcolors.highlight('passed', bcolors.OKGREEN)
                elif r['passed']:
                    result = bcolors.highlight('passed/dirty', bcolors.WARNING)
                else:
                    if r['finished'] == True:
                        print(f'Expected {bcolors.highlight(str(r["expected"]), bcolors.OKBLUE)}, Result {bcolors.highlight(str(r["result"]), bcolors.OKBLUE)}')
                    exception = r.get('test_exception')
                    if exception is None:
                        exception = r.get('scaffold_exception')
                    result = bcolors.highlight('FAILED' if exception is None else exception, bcolors.FAIL)
                name = r['test'] if r.get('iteration') is None else f"{r['test']} @ {r['iteration']}"
                print(name,'-', result)
            results.append(r)
            total["tests"]+=1
            for metric in ["passed","finished","clean","test_exception","scaffold_exception"]:
                if r.get(metric) is not None and r[metric] != False:
                    total[metric]+=1

            total["elapsed"]+=r["elapsed"]
    if current_file is not None:
        print()
    total["results"]=results
    return total
