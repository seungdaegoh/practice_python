#!/usr/bin/env python3
#from random import randint
import random
import string

from bslist import BSList

max_numbers = 500

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def t_max(count):

    list = BSList()

    for i in range(count):
        key = randomString()
        value = randomString()
        list.set( key, value )

t_max(10000)


def test_set():

    list = BSList()

    list.set("old", "C program")
    list.set("current", "Python")
    list.set("future", "AI")


def test_list():
    list = BSList()


    list.set("4current-1", "go lang")
    list.set("5current", "Python")


    list.set("1old", "C program")
    list.set("2current-3", "C++")
    list.set("3current-2", "java script")
    list.list("Added 5 Keys")

    list.set("6current+1", "deep learning")
    list.set("7current+2", "machine learning")
    list.set("8future", "AI")
    list.list("Print All ~~")


def test_get():

    list = BSList()

    list.set("old", "C program")
    list.set("current", "Python")
    list.set("future", "AI")

    print(list.get("old"))
    assert(list.get("old").value == "C program")
    print(list.get("future"))
    assert(list.get("future").value == "AI")
    assert(list.get("current").value == "Python")


def test_delete():

    list = BSList()

    list.set("old", "C program")
    list.delete("old")
    assert(list.count() == 0)
    list.list("__No nodes__#1")


    list.set("old", "C program")
    list.set("current", "Python")
    list.set("future", "AI")

    list.delete("old")
    list.list("Print two nodes ~~")

    print("OLD=", list.get("old"))
    assert(list.get("old") == None)

    list.delete("current")
    list.list("Print one nodes ~~")

    print("CURRENT=", list.get("current"))
    assert(list.get("current") == None)

    assert(list.count() == 1)
    list.delete("future")

    list.list("__No nodes__")

    list.set("1old", "C program")
    list.set("2current-3", "C++")
    list.set("3current-2", "java script")

    list.set("4current-1", "go lang")
    list.set("5current", "Python")

    list.set("6current+1", "deep learning")
    list.set("7current+2", "machine learning")
    list.set("8future", "AI")

    list.list("Print All ~~")

    assert(list.count() == 8)


'''
print("________SET_______")
test_set()
print("________LIST_______")
test_list()
test_get()
test_delete()
'''
