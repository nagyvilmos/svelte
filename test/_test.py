from datetime import datetime
import logging

log = logging.getLogger('migration')
log.setLevel(logging.DEBUG)

test_funcs = []

def test(description, scafold=None, cleanup=None):
    log.debug(f"wrap {description}")
    def test_decorator(test):
        def wrapper(test_name):
            if test_name is not None and test_name != description:
                return None
                
            log.info('=====Test: ' + description)
            doc = {
                'test':description,
                'passed':False,
                'finished':False,
                'started':datetime.now()}
            try:
                context=scafold() if scafold is not None else None
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
                doc['scafold_exception'] = str(ex)
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
