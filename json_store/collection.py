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


    def _insert_into_collection(self, records):
        col = self.store._data[self.name]
        ids = []
        for record in records:
            _id = record.get('_id')
            if _id is None:
                _id = str(uuid.uuid4())
                record['_id'] = _id
            elif any(x['_id'] == _id for x in col):
                raise KeyError
            ids.append(_id)
        print(col)
        col.extend(records)
        return ids

    def insert_one(self, record, save=True):
        response = self._insert_into_collection([record])
        self.store.commit(self.name, save)
        return response[0]

    def insert_many(self, records, save=True):
        ids = self._insert_into_collection(records)
        self.store.commit(self.name, save)
        return len(ids)
