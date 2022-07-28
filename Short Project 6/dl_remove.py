'''File: dl_remove.py.
   Author: Kareem Khalidi.
   Purpose: remove node from double
            linked list
   Course: CSC 120 1st Semester.
'''

from dlist_node import *

'''Summary: removes node from dll
   Arguments: head of list, node to remove
   Returns: head of list
   Assumptions: list is not empty
   Nothing else of interest
'''
def dl_remove(head, dead_node):
    if(dead_node.prev is None and dead_node.next is None):
        return(None)
    elif(dead_node.prev is None):
        head = head.next
        head.prev = None
        return(head)
    elif(dead_node.next is None):
        cur = dead_node.prev
        cur.next = None
        return(head)
    else:
        cur = dead_node
        temp = cur.prev
        cur = cur.next
        temp.next = cur
        cur.prev = temp
        return(head)