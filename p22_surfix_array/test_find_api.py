#!/usr/bin/env python3

from suffix_array import suffix_array 

def test_list():

    sa = suffix_array("abcdef")

    sa.list("initial test")
    print("done with initial test")
    return

def test_find_shortest():

    sa = suffix_array("abcddeeeeabcddeefghabcd")

    word = sa.find_shortest("abc")
    assert(word == "abcd")

    word = sa.find_shortest("azi")
    assert(word == None)

    return


def test_find_longest():

    sa = suffix_array("abcdeabcddeefghabcd")

    word = sa.find_longest("abc")
    assert(word == "abcdeabcddeefghabcd")

    word = sa.find_longest("azi")
    assert(word == None)
    return

def test_find_all():

    sa = suffix_array("abcdefabc")

    all_word = sa.find_all("abc")

    assert(all_word[0] == "abcdefabc")
    assert(all_word[1] == "abc")
    print("ALL_WORD=", all_word)


    all_word = sa.find_all("azi")
    assert(all_word == None)

    print("done with find_all")
    return

