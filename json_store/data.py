class Data:
    def __init__(self, source):
        self.source = source

    def list(self):
        return [x for x in self.source()]

    def has_content(self):
        for _ in self.source():
            return True
        return False
    
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

    def reduce(self, reduce):
        current_value = []
        for x in self.source():
            current_value = reduce(current_value, x)
        def reduced_data():
            for x in current_value:
                yield map(x)
        return Data(reduced_data)
