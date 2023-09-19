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

@test('insert single', True, create_collection, clear_collection)
def insert_single(collection):
    result = collection.insert({'a': 1}, True)
    return result is not None

@test('retrieve by id', 1, create_collection, clear_collection)
def retrieve_id(collection):
    result = collection.insert({'a': 1}, True)
    back = collection.get(id=result)

    return back.get('a') if back is not None else None

TEST_COUNT = 100
@test('insert many', TEST_COUNT, create_collection, clear_collection)
def insert_many(collection):
    data = [{'value' : x, 'even': x%2==0} for x in range(TEST_COUNT)]
    return collection.insert_many(data, True, False)

@test('retrieve by where', TEST_COUNT/2, create_collection, clear_collection)
def retrieve_where(collection):
    insert_many(collection)

    return len(collection.data().where({"even": True}).list())
