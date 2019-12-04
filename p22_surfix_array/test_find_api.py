#!/usr/bin/env python3

from suffix_array import suffix_array 

def test_list():

    sa = suffix_array("abcdef")

    sa.list("initial test")
    print("done with initial test")
    return

def test_find_shortest():

    return

def test_find_logest():

    return

def test_find_all():

    sa = suffix_array("abcdefabc")

    all_word = sa.find_all("abc")

    assert(all_word[0] == "abcdefabc")
    assert(all_word[1] == "abc")
    print("ALL_WORD=", all_word)
    print("done with find_all")
    return

