from ._test import test
from json_store.data import Data

def producer():
    def p():
        for x in range(10):
            yield x+1

    return Data(p)

@test("has content", producer)
def has_content(data:Data):
    return data.has_content()

@test("list contains all items", producer)
def list(data:Data):
    return len(data.list()) == 10

@test("filter list", producer)
def filter(data:Data):
    return len(data.filter(lambda x : x%3 == 0).list()) == 3

@test("reduce list", producer)
def reduce(data:Data):
    return data.reduce(lambda total,x: total+x, 0) == 55

@test("find prime numbers", producer)
def find_primes(data:Data):
    def find_prime(found, x):
        if x > 1:
            prime=True
            for y in found:
                if x%y == 0:
                    prime=False
            if prime:
                found.append(x)
        return found
    primes = data.reduce(find_prime, [])
    
    return primes == [2, 3, 5, 7]
