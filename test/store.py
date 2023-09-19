from ._test import test
from json_store import init_store, get_store
from random import randint
import os

def store_name():
    return f"test{randint(1000,10000)}.json"

def create_store():
    path = store_name()
    init_store(path)
    return get_store()

def close_store(store):
    store.close(False)
    if os.path.isfile(store.path):
        os.remove(store.path)
    return True

@test('create a store', True, create_store, close_store)
def create(store):
    return store is not None and store.open

@test('close store', True, create_store)
def close(store):
    store.close(False)
    return store is not None and not store.open
