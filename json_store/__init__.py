from .store import Store

store_handle: Store = None

def init_store(path, folder = False, save_action = None):
    global store_handle
    store_handle = Store(path, folder, save_action)

def close_store(commit:bool):
    store_handle.close(commit)
    store_handle = None

def get_store():
    return store_handle
