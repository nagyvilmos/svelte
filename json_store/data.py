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
                if is_match(x, filter):
                    return x
        return None
    
    def filter(self, filter):
        def filtered_data():
            found = False
            for x in self.source():
                if is_match(x, filter):
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
        if fields is None == function is None:
            raise ValueError("Must set one of fields or function")
        if fields is not None:
            # turn the fields into a function
            
            # do this once:
            field_compares=[]
            for field in fields:
                reverse_result = field[0] == '-'
                name = field[1:] if reverse_result else field
                compare = -1 if reverse_result else 1
                field_compares.append((name, compare))
            print(field_compares)
            def compare_by_fields(a,b):
                for name,compare in field_compares:
                    a_v = a.get(name)
                    b_v = b.get(name)
                    print(a_v, b_v)
                    if a_v == b_v:
                        return 0
                    if a_v is None:
                        return -compare
                    if b_v is None:
                        return compare
                    if a_v > b_v:
                        return compare
                    return -compare
                return 0
            return self.sort(None, compare_by_fields)

        items = self.list()

        list_len = len(items)
        order = list(range(list_len))


        # double ended sort,
        # moving it to start and finish means it is  O((n/2)^2) not O(n^2) 
        def sorted_data():
            swap_last = False
            z = list_len-1
            for x in range(list_len):
                y = z

                while y > x:
                    if function(items[order[y]],items[order[x]]) < 0:
                        temp=order[y]
                        order[y]=order[x]
                        order[x]=temp
                        print(x, items[temp])
                    if y < z and function(items[order[y]],items[order[z]]) > 0:
                        temp=order[y]
                        order[y]=order[z]
                        order[z]=temp
                        swap_last=True
                        print(z, items[temp])
                    y-=1
                if not swap_last:
                    z-=1
                swap_last=False
                yield items[order[x]]

        print(sorted_data)
        return Data(sorted_data)

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
