#!/usr/bin/env  python3

import sys

from dictionary import Dictionary

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def test_speed():
    print(__name__, "@"*25)
    print(sys._getframe().f_code.co_name)
    print(__name__, "@"*25)

    states = Dictionary()

    key = randomString()
    value = randomString()

    for i in range(10_000):
        key = randomString()
        value = randomString()

        print("KEY=", key, "VALUE=", value)
        states.set(key, value)
        get_value = states.get(key)
        assert(get_value == value)


def test_set():
    print(__name__, "@"*25)
    print(sys._getframe().f_code.co_name)
    print(__name__, "@"*25)
    states = Dictionary()
    states.set('Florida', 'FL')
    _state = states.get('Florida')

    assert(_state == 'FL')



'''
# create a mapping of state to abbreviation
states = Dictionary()
states.set('Oregon', 'OR')
states.set('Florida', 'FL')
states.set('California', 'CA')
states.set('New York', 'NY')
states.set('Michigan', 'MI')


# create a basic set of states and some cities in them
cities = Dictionary()
cities.set('CA', 'San Francisco')
cities.set('MI', 'Detroit')
cities.set('FL', 'Jacksonville')
cities.set('NY', 'New York')
cities.set('OR', 'Portland')
'''

'''
# print(every state abbreviation
print('-' * 10)
states.list()

# print(every city in state
print('-' * 10)
cities.list()

'''

if (__name__ == "__main__"):

    print("Hi")
    print("Name=", __name__)
    print("File=", __file__)
    print(dir())

    print("-" * 40)

    import ttt

    for i in dir(ttt):
        item = getattr(ttt, i)
        if callable(item):
#       print("__what?___", item)
            item()

    print("End of Job")
