import json, uuid, os.path
from .collection import Collection

class Store:
    def __init__(self, path:str, folder:bool = False, save_action:bool = None) -> None:
        self.path = path
        self.folder = folder
        self.save_action = save_action if save_action is not None else folder
        self._data = None
        self._changed = []

    def close(self, commit: bool):
        if commit:
            self.commit()
        
    def _load_data(self, path:str):
        if (not os.path.isfile(path)):
            return None

        with open(path, 'r') as f:
            a = f.readlines()
            t = ''.join(a)
            d = json.loads(t)
        return d

    def _save_data(self, path, data):
        with open(path, 'w') as f:
            f.write(json.dumps(data, default=str))

    def get(self, collection:str) -> Collection:
        if self._data == None or (self.folder and self._data.get(collection) == None):
            p = self.path if not self.folder else f"{self.path}/{collection}.json"
            d = self._load_data(p)

            if self.folder:
                if self._data is None:
                    self._data = {}
                self._data[collection] = d if d is not None else []
            else:
                self._data = d if d is not None else {}

        #if loaded
        return Collection(collection, self)

    def _depricated_get_data(self,collection,where=None,id=None):
        '''Get data from a collection
        
        Parameters:
            collection:name of the collection to be retrieved
            where (lambda):a function to select records; default is all records
            id (Any):the unique id of the record
        Returns:
            if no id is defined then all records that match otherwise the single record with a matching id
        '''

        if self._data == None or (self.folder and self._data[collection] == None):
            p = self.path if not self.folder else f"{self.path}/{collection}.json"
            d = self._load_data(p)

            if self.folder:
                if self._data is None:
                    self._data = {}
                self._data[collection] = d
            else:
                self._data = {} if d is None else d

        #if loaded

        col = self._data.get(collection,[])

        if id is not None:
            col = [x for x in col if x.get('_id') == id]
            return col[0] if len(col)>0 else None
        if where is not None:
            col = [x for x in col if where(x)]

        return col

    def _depricated_set(self, collection, data, append=True, save=None):
        '''Set data in a collection
        '''

        save_data = data
        if append:
            ## assumes less data then the collection:
            ids = [x.get('_id') for x in save_data if x.get('_id') is not None]
            for d in self.get(collection):
                if d.get('_id') is not ids:
                    save_data.append(d)
        
        save_data = [x for x in save_data if not x.get("_delete", False)]
        for d in save_data:
            if d.get('_id') is None:
                d['_id'] = str(uuid.uuid4())
        self._data[collection] = save_data 

        if collection not in self._changed:
            self._changed.append(collection)
        save_now = save if save is not None else self.folder
        if save_now:
            self.save()

    def commit(self, collection, save=None):
        if collection not in self._changed:
            self._changed.append(collection)
        save_now = save if save is not None else self.folder
        if save_now:
            self.save()

    def save(self):
        '''Save any changes to the database'''
        if len(self._changed) == 0:
            return

        if self.folder:
            for col in self._changed:
                p = f"{self.path}/{col}.json"
                self._save_data(p,self._data.get(col, []))
        else:
            self._save_data(self.path,self._data)

        self._changed = []

"""See if a doc matches a filter
match = {"field": {"compare", value}}
      | {"$and": [match, ...]}
      | {"$or": [match, ...]}
      | {"$not": match}
compare = "$eq"|"$ne"|"$lt"|"$gt"|"$le"|"$ge"|"$value"

{"$value" : true} checks the key exists and has a value
{"$value" : false} checks the key does not exist

To check if a key is set with no value:
{"$not": "$or": [{"field": {"$value" : false}}, {"field": {"$value" : true}}]}
"""
def is_match(doc, filter):
    if filter is None:
        return True

    if callable(filter):#
        return filter(doc)

    for key in filter.keys():
        value = filter[key] 

        compare = {
            "$and": lambda v : not([is_match(doc, x) for x in v].any(False)),
            "$or": lambda v  : [is_match(doc, x) for x in v].any(True),
            "$not": lambda v : not is_match(doc, v)
        }.get(key)
        if compare is not None :
            return compare(doc, value)
        if filter[key] != doc.get(key):
            return False
    
    return True



