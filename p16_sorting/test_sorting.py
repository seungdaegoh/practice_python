#!/usr/bin/env python3


import sorting
from dllist import DoubleLinkedList
from random import randint

max_numbers = 5

def random_list(count):

    numbers = DoubleLinkedList()

    for i in range(count):
        numbers.push( randint(1, 100) )

    numbers.dump("after random_list()")
    return numbers


def is_sorted(numbers):

    for i in range(numbers.count() - 1):
        if (numbers.get(i) >= numbers.get(i + 1)):
            return False

    return True

'''
def test_bubble_sort():
    numbers = random_list(max_numbers)
    sorting.bubble_sort(numbers)

    numbers.dump("after bubble_sort()")

    assert is_sorted(numbers)
'''

def test_merge_sort():
    numbers = random_list(max_numbers) 
    sorting.merge_sort(numbers)

    numbers.dump("after sort()")
    assert is_sorted(numbers)


'''
def test_quick_sort():
    numbers = random_list(max_numbers)
    sorting.quick_sort(numbers, 0, numbers.count() - 1)
    assert is_sorted(numbers)
'''
