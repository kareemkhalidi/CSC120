'''File: dl_insert.py.
   Author: Kareem Khalidi.
   Purpose: insert nodes into double
            linked list
   Course: CSC 120 1st Semester.
'''

from dlist_node import *

'''Summary: inserts node into dll before the
            specified node
   Arguments: head of list, node to place before,
              node to insert
   Returns: head of dll
   Assumptions: list is not empty
   Nothing else of interest
'''
def dl_insert_before(head, old_node, new_node):
    if(head == old_node):
        head.prev = new_node
        new_node.next = head
        head = head.prev
        return(head)
    temp = old_node.prev
    temp.next = new_node
    old_node.prev = new_node
    new_node.prev = temp
    new_node.next = old_node
    return(head)

'''Summary: inserts node into dll after the
            specified node
   Arguments: head of list, node to place after,
              node to insert
   Returns: head of dll
   Assumptions: list is not empty
   Nothing else of interest
'''
def dl_insert_after(head, old_node, new_node):
    if(old_node.next is None):
        old_node.next = new_node
        new_node.prev = old_node
        return(head)
    temp = old_node.next
    temp.prev = new_node
    old_node.next = new_node
    new_node.prev = old_node
    new_node.next = temp
    return(head)