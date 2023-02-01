from ._test import test
from json_store.data import Data
import os

def producer():
    def p():
        for x in range(10):
            yield x

    return Data(p)

@test("has content", producer)
def test_has_content(data:Data):
    return data.has_content()

@test("list", producer)
def test_list(data:Data):
    return len(data.list()) == 10

@test("filter", producer)
def test_filter(data:Data):
    return len(data.filter(lambda x : x%3 == 0).list()) == 4

@test("reduce", producer)
def test_reduce(data:Data):
    return len(data.filter(lambda x : x%3 == 0).list()) == 4
