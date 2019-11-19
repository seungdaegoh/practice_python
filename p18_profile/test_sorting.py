#!/usr/bin/env python3


import sorting
from dllist import DoubleLinkedList
from random import randint

max_numbers = 500

def random_list(count):

    numbers = DoubleLinkedList()

    for i in range(count):
        numbers.push( randint(1, max_numbers * 10) )

     #numbers.dump("after adding random_list()")
    return numbers


def is_sorted(numbers):

    for i in range(numbers.count() - 1):
        if (numbers.get(i) > numbers.get(i + 1)):
            return False

    return True

def test_bubble_sort():
    numbers = random_list(max_numbers)
    sorting.bubble_sort(numbers)

     #numbers.dump("after bubble_sort()")

    assert is_sorted(numbers)
    print("OK bubble_sort()")

def test_merge_sort():
    numbers = random_list(max_numbers) 
    sorting.merge_sort(numbers)

     #numbers.dump("after merge_sort()")
    assert is_sorted(numbers)
    print("OK merge_sort()")


'''
def test_quick_sort():
    numbers = random_list(max_numbers)
    sorting.quick_sort(numbers, 0, numbers.count() - 1)
    assert is_sorted(numbers)
'''



if __name__ == '__main__' :

    test_bubble_sort()
    test_merge_sort()
    
