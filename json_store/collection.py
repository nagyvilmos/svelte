from decimal import InvalidContext
import json, uuid, os.path
from .data import Data

class Collection:
    def __init__(self, name, store) -> None:
        self.name = name
        self.store = store
        #nb: this now does not hold data but does know how to get it.

    def data(self):
        col = self.store._data[self.name]
        def data():
            for x in col:
                yield x
        return Data(data)

    def get(self, where=None, id=None):
        return None

    def _insert_into_collection(self, records, save=None):
        col = self.store._data.get(self.name)
        if (col is None):
            col = []
            self.store._data[self.name] = col
        ids = []

        for record in records:
            _id = record.get('_id')
            if _id is None:
                _id = str(uuid.uuid4())
                record['_id'] = _id
            elif any(x['_id'] == _id for x in col):
                raise KeyError
            ids.append(_id)

        col.extend(records)
        self.store.commit(self.name, save)
        return ids

    def insert(self, record, save=None):
        response = self._insert_into_collection([record], save)
        return response[0]

    def insert_all(self, records, save=None, return_ids = True):
        ids = self._insert_into_collection(records, save)
        return ids if return_ids else len(ids)
