from ._test import test
from json_store import  init_store
import os

def store_name():
    return "test.json"

@test('create a store', store_name)
def create_store(path):
    init_store(path, False)
    return not os.path.isfile(path)

