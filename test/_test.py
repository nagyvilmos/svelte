from datetime import datetime
import logging
import traceback
#logging.basicConfig(level=logging.WARNING)
log = logging.getLogger('test')
log.setLevel(logging.DEBUG)

test_funcs = []

def test(expected:any=True, setup=None, cleanup=None, included=True, iterator=None):
    def test_decorator(test):
        def wrapper(test_list, file_list):
            
            test_name = test.__name__
            if test_list is not None and \
                    test_name not in test_list:
                return None
            
            file_name = test.__globals__['__file__'].split('\\')[-1].split('.')[0]
            if file_list is not None and \
                    file_name not in file_list:
                return None
            
            if not included and test_list is None and file_list is None:
                # test requires explicit include
                return None
            description = test.__name__
            log.info('=====Test: ' + description)
            def run_test(expected_result, iteration):
                doc = {
                    'test': test_name,
                    'expected': expected_result,
                    'file': file_name,
                    'description':description,
                    'passed':False,
                    'finished':False,
                    'started':datetime.now()}
                if iteration is not None:
                    doc['iteration'] = iteration
                try:
                    context=None
                    if setup is None:
                        context=iteration
                    elif iteration is None:
                        context=setup()
                    else:
                        context=setup(iteration)

                    try:
                        result = test(context) if context is not None else test()
                        doc['result']=result
                        doc['passed']=result == expected_result
                        doc['finished']=True
                    except Exception as ex:
                        doc['test_exception'] = ex
                        doc['test_traceback'] = traceback.format_exc()
                        doc['passed']=False
                        doc['finished']=False

                    clean=cleanup(context) if cleanup is not None else True
                    doc['clean']=clean
                except Exception as ex:
                    doc['scaffold_exception'] = ex
                    doc['scaffold_traceback'] = traceback.format_exc()
                    doc['clean']=False
                doc['completed'] = datetime.now()
                doc['elapsed'] = (doc['completed'] - doc['started']).total_seconds()
                return doc
            
            if iterator is None:
                return [run_test(expected, None)]
            else:          
                return [run_test(x[1], x[0]) for x in iterator()]

        # add the wrapper to the list of migrations
        # if it hasn't already been called, then it will
        # be called once and recorded in the database
        test_funcs.append(wrapper)
        return test
    return test_decorator
