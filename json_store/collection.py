import uuid
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

    def get(self, id):
        return self.data().find(lambda x : x['_id'] == id)

    def list(self):
        return self.data().list()

    def has_content(self):
        return self.data().has_content()
    
    def find(self, filter):
        return self.data().find()
    
    def filter(self, filter):
        return self.data().filter(filter)
    
    def map(self, map):
        return self.data().map(map)

    def reduce(self, reduce, initial_value = None):
        return self.data().list(reduce, initial_value)

    def filter(self, where):
        return self.data().filter(where)

    def find(self, where):
        return self.data().find(where)
    
    def _insert_into_collection(self, records, save, replace):
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
                if not replace:
                    raise KeyError
                raise KeyError
            ids.append(_id)

        col.extend(records)
        self.store.commit(self.name, save)
        return ids

    def insert(self, record, save=None, replace=False):
        response = self._insert_into_collection([record], save, replace)
        return response[0]

    def insert_many(self, records, save=None, return_ids = True, replace=False):
        ids = self._insert_into_collection(records, save, replace)
        return ids if return_ids else len(ids)

