from ._test import test
from json_store import init_store, get_store
from random import randint
import os

def store_name():
    return f"test{randint(1000,10000)}.json"

def create_collection():
    path = store_name()
    init_store(path)
    return get_store().get("test")

def clear_collection(collection):
    collection.store.close(False)
    if os.path.isfile(collection.store.path):
        os.remove(collection.store.path)
    return True

@test('insert single', create_collection, clear_collection)
def insert_single(collection):
    result = collection.insert({'a': 1}, True)
    return result is not None

@test('retrieve by id', create_collection, clear_collection)
def retrieve_id(collection):
    result = collection.insert({'a': 1}, True)
    back = collection.get(id=result)

    return back is not None and back['a'] == 1
