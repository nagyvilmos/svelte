import json
import os.path
from .collection import Collection


class StoreException(Exception):
    def __init__(self, massage: str = "Store exception", path: str = ""):
        super(massage)


class Store:
    def __init__(self, path: str, folder: bool = False, save_action: bool = None) -> None:
        self.path = path
        self.folder = folder
        self.save_action = save_action if save_action is not None else folder
        self._data = None
        self._changed = []
        self.open = True

    def close(self, commit: bool):
        if commit:
            self.commit()
        self._data = None
        self.open = False

    def _load_data(self, path: str):
        if not self.open:
            raise StoreException('Store is not open')
        if (not os.path.isfile(path)):
            return None

        with open(path, 'r') as f:
            a = f.readlines()
            t = ''.join(a)
            d = json.loads(t)
        return d

    def _save_data(self, path, data):
        if not self.open:
            raise StoreException('Store is not open')
        with open(path, 'w') as f:
            f.write(json.dumps(data, default=str))

    def get(self, collection_name: str) -> Collection:
        if self._data == None or (self.folder and self._data.get(collection_name) == None):
            p = self.path if not self.folder else f"{self.path}/{collection_name}.json"
            d = self._load_data(p)

            if self.folder:
                if self._data is None:
                    self._data = {}
                self._data[collection_name] = d if d is not None else []
            else:
                self._data = d if d is not None else {}

        # if loaded
        return Collection(collection_name, self)

    def commit(self, collection_name:str, save:bool=None):
        if not self.open:
            raise StoreException('Store is not open')
        if collection_name not in self._changed:
            self._changed.append(collection_name)
        save_now = save if save is not None else self.folder
        if save_now:
            self.save()

    def save(self):
        '''Save any changes to the database'''
        if not self.open:
            raise StoreException('Store is not open')
        if len(self._changed) == 0:
            return

        if self.folder:
            for col in self._changed:
                p = f"{self.path}/{col}.json"
                self._save_data(p, self._data.get(col, []))
        else:
            self._save_data(self.path, self._data)

        self._changed = []
