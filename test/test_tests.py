from random import random
from time import sleep
from ._test import test
# use this module to test the testing framework


#@test('This must fail')
def failed_test():
    sleep(.456)
    return False

#@test('This could fail')
def random_failure():
    value=random()
    sleep(value)
    return value>.666

#@test('Throw an exception')
def exception():
    raise NotImplementedError("Exception in test") 
    return True

def scafold_exception():
    raise NotImplementedError("Exception in scafold") 

#@test('Scafold error', scafold=scafold_exception)
def error_scafold():
    return True

def cleanup_fail(ctx):
    return False

#@test('Cleanup fail', cleanup=cleanup_fail)
def fail_cleanup():
    return True

def cleanup_exception(ctx):
    raise NotImplementedError("Exception in cleanup") 

#@test('Cleanup error', cleanup=cleanup_exception)
def error_cleanup():
    return True
