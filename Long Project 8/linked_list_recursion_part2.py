'''File: linked_list_recursion_part2.py.
   Author: Kareem Khalidi.
   Purpose: Practice with recursion and linked lists
   Course: CSC 120 1st Semester.
'''

from list_node import *

'''Summary: recursively turns an array into a linked list
   Arguments: array
   Returns: head of linked list
   Assumptions: None
   Nothing else of interest
'''
def array_to_list_recursive(data):
    if(len(data) == 0):
        return(None)
    else:
        head = ListNode(data[0])
        head.next = array_to_list_recursive(data[1:])
        return(head)

'''Summary: recursively takes every other value of a linked list
            starting with the second value
   Arguments: head
   Returns: head
   Assumptions: None
   Nothing else of interest
'''
def accordion_recursive(head):
    if(head is None):
        return(None)
    elif(head.next is None):
        return(None)
    else:
        head = head.next
        head.next = accordion_recursive(head.next)
        return(head)

'''Summary: takes 2 linked lists and creates a new list with both values
   Arguments: head1, head2
   Returns: head
   Assumptions: None
   Nothing else of interest
'''
def pair_recursive(head1, head2):
    if(head1 is None or head2 is None):
        return(None)
    elif(head1.next is None or head2.next is None):
        return(ListNode((head1.val, head2.val)))
    else:
        head = ListNode((head1.val, head2.val))
        head.next = pair_recursive(head1.next, head2.next)
        return(head)