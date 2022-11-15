from .store import Store

store_handle: Store = None

def init_store(path, folder = False, save_action = None):
    global store_handle
    store_handle = Store(path, folder, save_action)

def get_store():
    return store_handle
