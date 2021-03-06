#!/usr/bin/env python3
#from random import randint
import random
import string

from bstree import BSTree

max_numbers = 500

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def t_max(count):
    tree = BSTree()

    for i in range(count):
        key = i #randomString()
        value = i#randomString()
        tree.set( key, value )

    print("done  set()")

    for i in range(count):
        key = i #randomString()
        node = tree.get( key )
        assert( key == node.value)


if (__name__ == "__main__"):
    import sys

    print(sys.argv[1])
    
    t_max(int(sys.argv[1]))





def test_set():

    tree = BSTree()

    tree.set("old", "C program")
    tree.set("current", "Python")
    tree.set("future", "AI")


def test_list():
    tree = BSTree()


    tree.set("4current-1", "go lang")
    tree.set("5current", "Python")


    tree.set("1old", "C program")
    tree.set("2current-3", "C++")
    tree.set("3current-2", "java script")
    tree.list(None, "Added 5 Keys")

    tree.set("6current+1", "deep learning")
    tree.set("7current+2", "machine learning")
    tree.set("8future", "AI")
    tree.list(None, "Print All ~~")


def test_get():

    tree = BSTree()

    tree.set("old", "C program")
    tree.set("current", "Python")
    tree.set("future", "AI")

    print(tree.get("old"))
    assert(tree.get("old").value == "C program")
    print(tree.get("future"))
    assert(tree.get("future").value == "AI")
    assert(tree.get("current").value == "Python")


def test_delete():

    tree = BSTree()

    tree.set("old", "C program")
    tree.delete("old")
    assert(tree.count() == 0)
    tree.list(None, "__No nodes__#1")


    tree.set("old", "C program")
    tree.set("current", "Python")
    tree.set("future", "AI")

    tree.delete("old")
    tree.list(None, "Print two nodes ~~")

    print("OLD=", tree.get("old"))
    assert(tree.get("old") == None)

    tree.delete("current")
    tree.list(None, "Print one nodes ~~")

    print("CURRENT=", tree.get("current"))
    assert(tree.get("current") == None)

    assert(tree.count() == 1)
    tree.delete("future")

    tree.list(None, "__No nodes__")

    tree.set("1old", "C program")
    tree.set("2current-3", "C++")
    tree.set("3current-2", "java script")

    tree.set("4current-1", "go lang")
    tree.set("5current", "Python")

    tree.set("6current+1", "deep learning")
    tree.set("7current+2", "machine learning")
    tree.set("8future", "AI")

    tree.list(None, "Print All ~~")

    assert(tree.count() == 8)

#test_delete()
