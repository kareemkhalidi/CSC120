'''File: linked_list_recursion.py.
   Author: Kareem Khalidi.
   Purpose: to improve skills with linked lists 
            and recursion
   Course: CSC 120 1st Semester.
'''

from list_node import *

'''Summary: returns true if linked list
            is sorted and false if not
   Arguments: head
   Returns: boolean
   Assumptions: None
   Nothing else of interest
'''
def is_sorted(head):
    cur = head
    if(cur is None):
        return(True)
    elif(cur.next is None):
        return(True)
    else:
        while(cur.next is not None):
            if(cur.next.val < cur.val):
                return(False)
            cur = cur.next
        return(True)

'''Summary: returns true if linked list is
            sorted and false if not
   Arguments: head
   Returns: boolean
   Assumptions: None
   Nothing else of interest
'''
def is_sorted_recursive(head):
    cur = head
    if(cur is None):
        return(True)
    elif(cur.next is None):
        return(True)
    else:
        return(cur.val <= cur.next.val and is_sorted_recursive(cur.next))