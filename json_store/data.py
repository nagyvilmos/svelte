"""
Data class for json_store

The data is, in general, accesssed via an iterator

"""
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

    """
    Sort the data based on the supplied comparison
    
    The comparison may be a function that takes two json objects and returns a numeric value; negative for first, positive for second and zero for equal 
    Alternatively it can be json array of field names; field names may be prefixed with '-' to indicate descending order.

    Returns a sorted data object.
    """
    def sort(self, comparison):
        if comparison is None:
            raise ValueError("Must provide a sort order")
        if not callable(comparison):
            # turn the fields into a function
            # do this once:
            field_compares=[]
            for field in comparison:
                reverse_result = field[0] == '-'
                name = field[1:] if reverse_result else field
                compare = -1 if reverse_result else 1
                field_compares.append((name, compare))
            def compare_by_fields(a,b):
                for name,compare in field_compares:
                    a_v = a.get(name)
                    b_v = b.get(name)
                    if a_v == b_v:
                        continue
                    if a_v is None:
                        return -compare
                    if b_v is None:
                        return compare
                    if a_v > b_v:
                        return compare
                    return -compare
                return 0
            return self.sort(compare_by_fields)

        items = self.list()

        list_len = len(items)
        order=list(range(list_len))

        gap=list_len
        sorted=False

        while not sorted:
            gap=int(gap/1.3)
            if gap <= 1:
                gap=1
                sorted=True #If there are no swaps this pass, we are done
            x = 0
            while x+gap < list_len:
                y = x+gap
                if comparison(items[order[y]],items[order[x]]) < 0:
                    temp=order[x]
                    order[x]=order[y]
                    order[y]=temp
                    sorted=False
                    # If this assignment never happens within the loop,
                    # then there have been no swaps and the list is sorted.
                x+=1

        def sorted_data():
            for x in order:
                yield items[x]

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
