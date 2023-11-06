from ._test import test
from json_store import init_store, get_store, Store
from random import randint
import os

def store_name(folder):
    name = f"test{randint(1000,10000)}"
    return name if folder else f"{name}.json"

def create_store(folder) -> Store:
    path = store_name(folder)
    #print(path)
    init_store(path,folder)
    return get_store()

def close_store(store):
    store.close(False)
    if store.folder:
        if os.path.isdir(store.path):
            for file in os.listdir(store.path):
                os.remove(file)
            os.rmdir(store.path)
    elif os.path.isfile(store.path):
        os.remove(store.path)
    return True

def store_type():
    return [(x == 1, True) for x in range(2)]

@test('create a store', setup=create_store, cleanup=close_store, iterator=store_type)
def create(store):
    return store is not None and store.open

@test('close store', None, setup=create_store, iterator=store_type)
def close_store(store):
    store.close(False)
    return store is not None and not store.open

@test('write and read back', setup=create_store, cleanup=close_store, iterator=store_type)
def write_and_read_back(store:Store):
    test = store.get('test')
    test.insert({'x':1})
    store.commit('test',True)
    retrieve = store.get('test').find(lambda s: s['x'] == 1)
    print(test.list(), retrieve)
    return retrieve['x'] == 1