class Data:
    def __init__(self, source):
        self.source = source

    def __str__(self) -> str:
        return str(self.list())
    
    def list(self):
        return [x for x in self.source()]

    def has_content(self):
        for _ in self.source():
            return True
        return False
    
    def find(self, filter):
        for x in self.source():
                if filter(x):
                    return x
        return None
    
    def filter(self, filter):
        def filtered_data():
            found = False
            for x in self.source():
                if filter(x):
                    found = True
                    yield x
            if not found:
                yield from ()
        return Data(filtered_data)
    
    def map(self, map):
        def mapped_data():
            for x in self.source():
                yield map(x)
        return Data(mapped_data)

    def reduce(self, reduce, initial_value = None):
        current_value = initial_value
        for x in self.source():
            current_value = reduce(current_value, x)
        return current_value

    def sort(self, fields=None, function=None):
        pass
    
    def where(self, where):
        return self.filter(lambda x : is_match(x, where))

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

    if callable(filter):
        return filter(doc)
        
    #print(doc, filter)

    for key in filter.keys():
        value = filter[key] 
        compare = {
            "$and": lambda doc, v : all([is_match(doc, x) for x in v]),
            "$or":  lambda doc, v : any([is_match(doc, x) for x in v]),
            "$not": lambda doc, v : not is_match(doc, v)
        }.get(key)

        if compare is not None :
            return compare(doc, value)
        if value != doc.get(key):
            return False
    
    return True
