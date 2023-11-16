from random import random
from time import sleep
from ._test import test

"""Test harness tests

A series of tests for testing the validity of the test harness.
To use, replace #@test with @test
"""


@test(True, included=False)
def pass_test():
    sleep(random())
    return True


@test(True, included=False)
def failed_test():
    sleep(random())
    return False


@test(True, included=False)
def random_failure():
    value = random()
    sleep(value*2)
    if value > .666:
        raise NotImplementedError("Value too big - " + str(value))
    return value > .166


@test(True, included=False)
def exception():
    sleep(random())
    raise NotImplementedError("Exception in test")


def setup_exception():
    raise NotImplementedError("Exception in setup")


@test(setup=setup_exception, included=False)
def error_setup():
    sleep(random())
    return True


def cleanup_fail(ctx):
    return False


@test(cleanup=cleanup_fail, included=False)
def fail_cleanup():
    sleep(random())
    return True


def cleanup_exception(ctx):
    raise NotImplementedError("Exception in cleanup")


@test(cleanup=cleanup_exception, included=False)
def error_cleanup():
    sleep(random())
    return True


@test(cleanup=cleanup_exception, included=False)
def failed_error_cleanup():
    sleep(random())
    return False


@test('foo_bar', included=False)
def return_foo_bar():
    return 'foo_bar'


def ten_times():
    return [(x, x) for x in range(10)]


@test(included=False, iterator=ten_times)
def multiple(x):
    return x if x != 5 else 0


def square(r):
    return r*r


def nothing(r):
    return True


def five_times():
    return [(x+1, (x+1)*(x+1)) for x in range(5)]


@test(included=False, setup=square, cleanup=nothing, iterator=five_times)
def tests_with_setup_and_cleanup(x):
    return x
