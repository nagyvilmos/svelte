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
    store.close()
    if os.path.isfile(store.path):
        os.remove(store.path)

@test('create a store', create_store, close_store)
def test_create(store):
    return store is not None and store.open

@test('close store', create_store)
def test_close(store):
    store.close(False)
    return store is not None and not store.open

@test('write and retrieve', create_store, close_store)
def test_create(store):
    store.put()
