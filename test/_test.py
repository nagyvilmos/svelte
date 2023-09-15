from datetime import datetime
import logging
#logging.basicConfig(level=logging.WARNING)
log = logging.getLogger('test')
log.setLevel(logging.DEBUG)

test_funcs = []

def test(description, setup=None, cleanup=None, included=True):
    log.debug(f"wrap {description}")
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

            log.info('=====Test: ' + description)
            doc = {
                'test': test_name,
                'file': file_name,
                'description':description,
                'passed':False,
                'finished':False,
                'started':datetime.now()}
            try:
                context=setup() if setup is not None else None
                try:
                    doc['passed']=test(context) if context is not None else test()
                    doc['finished']=True
                except Exception as ex:
                    doc['test_exception'] = str(ex)
                    doc['passed']=False
                    doc['finished']=False
                clean=cleanup(context) if cleanup else True
                doc['clean']=clean
            except Exception as ex:
                doc['scaffold_exception'] = str(ex)
                doc['clean']=False
            doc['completed'] = datetime.now()
            doc['elapsed'] = (doc['completed'] - doc['started']).total_seconds()
            return doc

        # add the wrapper to the list of migrations
        # if it hasn't already been called, then it will
        # be called once and recorded in the database
        test_funcs.append(wrapper)
        return test
    return test_decorator
