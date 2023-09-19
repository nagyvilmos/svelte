from random import random
from time import sleep
from ._test import test

"""Test harness tests

A series of tests for testing the validity of the test harness.
To use, replace #@test with @test
"""

@test('Check you can pass', True, included=False)
def pass_test():
    sleep(random())
    return True

@test('This must fail', True,included=False)
def failed_test():
    sleep(random())
    return False

@test('This could fail',True, included=False)
def random_failure():
    value=random()
    sleep(value*2)
    return value>.333

@test('Throw an exception',True, included=False)
def exception():
    sleep(random())
    raise NotImplementedError("Exception in test") 
    

def setup_exception():
    raise NotImplementedError("Exception in setup") 

@test('Setup error', True,setup=setup_exception, included=False)
def error_setup():
    sleep(random())
    return True

def cleanup_fail(ctx):
    return False

@test('Cleanup fail', True,cleanup=cleanup_fail, included=False)
def fail_cleanup():
    sleep(random())
    return True

def cleanup_exception(ctx):
    raise NotImplementedError("Exception in cleanup") 

@test('Cleanup error', True,cleanup=cleanup_exception, included=False)
def error_cleanup():
    sleep(random())
    return True

@test('Passes expected foo_bar', 'foo_bar', included=False)
def return_foo_bar():
    return 'foo_bar'