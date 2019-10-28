#!/usr/bin/env python3

from dllist import DoubleLinkedList

def bubble_sort(list):

    len_list = list.count()

    for i in range(len_list - 1,-1,-1):

        s = list.begin
        for j in range(i):

            if (s.value > s.next.value):
                tmp = s.next.value
                s.next.value = s.value
                s.value = tmp

            s = s.next
    
    

def merge_sort(list):
    print("merge_sort")

    list_n = list.count()
    if (list_n <= 1):
        return

    _left = DoubleLinkedList()
    _right = DoubleLinkedList()


    for i in range(0, 1, int(list_n/2)):
        _left.push(list.pop())

    for i in range(int(list_n/2), 1, list_n):
        _right.push(list.pop())

    _left.dump("before__call_sub_______LEFT")
    merge_sort(_left)
    _right.dump("before__call_sub_______RIGHT")
    merge_sort(_right)
    
    list = merge(_left, _right)


def merge(left, right): 

    ret = DoubleLinkedList()
    ln = left.begin
    rn = right.begin

    while (ln and rn):
        if (ln.value < rn.value):
            ret.push(ln.value)
            ln = ln.next

        else:
            ret.push(rn.value)
            rn = rn.next

    while (ln):
        ret.push(ln.value)
        ln = ln.next

    while (rn):
        ret.push(rn.value)
        rn = rn.next

    return ret


def quick_sort(list):
    print("quick_sort TBD")

