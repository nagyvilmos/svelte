from ._test import test
from json_store.data import Data
from functools import reduce

def producer():
    def p():
        for x in range(10):
            yield x+1

    return Data(p)

@test("has content", True, producer)
def has_content(data:Data):
    return data.has_content()

@test("list contains all items", 10,producer)
def list(data:Data):
    return len(data.list()) 

@test("filter list", 3, producer)
def filter(data:Data):
    return len(data.filter(lambda x : x%3 == 0).list()) 

@test("reduce list", 55, producer)
def reduce_list(data:Data):
    return data.reduce(lambda total,x: total+x, 0)

@test("find prime numbers", [2, 3, 5, 7], producer)
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
    return data.reduce(find_prime, [])

from random import shuffle
def people():
    first_names = [
        'Ariel',
        'Violet',
        'Lena',
        'Emaline',
        'Liliana',
        'Jayden',
        'Ben',
        'Liam',
        'Atticus',
        'Lucas']
    shuffle(first_names)
    last_names = [
        'Grimm',
        'Skelton',
        'Fang',
        'Finch',
        'Smith',
        'Vargas',
        'Sweeney',
        'Strange',
        'Sisk',
        'Poindexter']
    shuffle(last_names)

    # print(len(first_names), first_names)
    # print(len(last_names), last_names)
 
    def p():
        for x in range(10):
            first = x%10
            last = (x-first)//10
            value = {
                'first_name':first_names[first],
                'last_name':last_names[last],
                'age': 5*len(last_names[last])+len(first_names[first])
            }
            yield value

    return Data(p)

@test("How many people are called Atticus or Poindexter?", 19, people)
def atticus_poindexter(data):
    return len(data.filter({'$or': [{'first_name': 'Atticus' }, {'last_name': 'Poindexter' }]}).list())

@test("How old is Atticus finch?", 32, people)
def find_entry(data:Data):
    found = data.find({'$and': [{'first_name': 'Atticus' }, {'last_name': 'Finch' }]})
    return found['age']

@test("Sorted by function", True, people)
def sorted_function(data):
    sorted=data.sort(function=lambda a,b : -2 if a['last_name'] < b['last_name'] \
                      else 2 if a['last_name'] > b['last_name'] \
                       else -1 if a['first_name'] < b['first_name'] \
                        else 1 if a['first_name'] > b['first_name'] \
                         else 0)

    def check(current,next):
        if current is None:
            return current
        if current['last_name']+current['first_name'] < next['last_name']+next['first_name']:
            return next
        return None
    
    return reduce(check,sorted.list(),{'first_name':'','last_name':''}) is not None

@test("Sorted by fields", {'first_name':'','last_name':''}, people)
def sorted_fields(data):
    sorted=data.sort(['-age', 'first_name']).list()
    for x in sorted:
        print(x)
    return sorted[0]
