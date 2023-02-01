from ._test import test
from json_store import init_store, get_store
import os

def store_name():
    return "test.json"

def create_store():
    path = store_name()
    init_store(path)
    return get_store()

def close_store(store):
    store.close()
    
@test('create a store', store_name)
def test_create(store):
    return store is not None and store

