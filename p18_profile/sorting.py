#!/usr/bin/env python3

from dllist import DoubleLinkedList

def bubble_sort(list):

    len_list = list.count()

    for i in range(len_list - 1, -1, -1):

        s = list.begin
        for j in range(i):

            if (s.value > s.next.value):
                tmp = s.next.value
                s.next.value = s.value
                s.value = tmp

            s = s.next
    
    

def merge_sort(list, lvl=0):
     #print("merge_sort")

    list_n = list.count()
    if (list_n <= 1):
        return

    _left = DoubleLinkedList()
    _right = DoubleLinkedList()


    #print("list_N:", list_n)
    for i in range(0, int(list_n/2), 1):
         #print("__Left:", i)
        _left.push(list.pop())

    for i in range(int(list_n/2), list_n, 1):
         #print("__Right:", i)
        _right.push(list.pop())

     #_left.dump("\t"*3*lvl +  "before__sort____LEFT")
    merge_sort(_left, lvl + 1)
     #_left.dump("\t"*3*lvl +  "after___sort____LEFT")

     #_right.dump("\t"*3*lvl + "before__sort____RIGHT")
    merge_sort(_right, lvl + 1)
     #_right.dump("\t"*3*lvl + "after___sort____RIGHT")
    
     #_left.dump("\t"*3*lvl +   "________LEFT")
     #_right.dump("\t"*3*lvl +  "________RIGHT")

    merge(_left, _right, list)

     #list.dump("\t"*3*lvl +  "after__merge(Left,Right)________")


def merge(left, right, ret): 

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

     #ret.dump("_______add L+R ______ :")



def quick_sort(list):
    print("quick_sort TBD")

