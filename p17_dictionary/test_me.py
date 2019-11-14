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

    for i in range(3):
        key = randomString()
        value = randomString()

        print("<<KEY=", key, "VALUE=", value, ">>")
        states.set(key, value)
        get_value = states.get(key)
        assert(get_value == value)

    states.list()


def test_set():
    print(__name__, "@"*25)
    print(sys._getframe().f_code.co_name)
    print(__name__, "@"*25)
    states = Dictionary()
    states.set('Florida', 'FL')


def test_get():
    print(__name__, "@"*25)
    print(sys._getframe().f_code.co_name)
    print(__name__, "@"*25)
    states = Dictionary()
    states.set('Oregon', 'OR')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')

    _state = states.get('Oregon')
    assert(_state == 'OR')
	
    _state = states.get('Michigan')
    assert(_state == 'MI')
	
    _state = states.get('New York')
    assert(_state == 'NY')


def test_remove():
    print(__name__, "@"*25)
    print(sys._getframe().f_code.co_name)
    print(__name__, "@"*25)
    states = Dictionary()
    states.set('Oregon', 'OR')

    states.set('California', 'CA')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')

    states.list()

    _state = states.get('New York')
    assert(_state == 'NY')

    states.delete("New York")
    states.delete("Oregon")

    states.list()
    _state = states.get('Oregon')
    assert(_state == None)
	
    _state = states.get('New York')
    assert(_state == None)
	
	



if (__name__ == "__main__"):

    print("Hi")
    req_version = (3,6)
    sys_version = sys.version_info
    print("REQ_V=", req_version, "SYS_VER=", sys_version)
    print("REQ_V <= SYS_VER ? =", req_version <= sys_version)

    print("Name=", __name__)
    print("File=", __file__)
    print(dir())

    print("-" * 40)

    import test_me

    for i in dir(test_me):
        item = getattr(test_me, i)
        if callable(item):
            print("__what?___", item)
            item()

    print("End of Job")
