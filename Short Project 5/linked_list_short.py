'''File: linked_list_short.py.
   Author: Kareem Khalidi.
   Purpose: 4 methods to manipulate linked lists
   Course: CSC 120 1st Semester.
'''

from list_node import *

'''Summary: Returns an array that represents a linked list
   Arguments: Head of list
   Returns: Array
   Assumptions: None
   Nothing else of interest
'''
def list_to_array(head):
    list_array = []
    if(head is not None):
        while(head.next is not None):
            list_array.append(head.val)
            head = head.next
        list_array.append(head.val)
    return(list_array)

'''Summary: Returns a linked list that represents an array
   Arguments: array
   Returns: head of linked list
   Assumptions: None
   Nothing else of interest
'''
def array_to_list(data):
    head = None
    if(len(data) > 0):
        head = ListNode(data[0])
        cur = head
        for i in range(len(data) - 1):
            cur.next = ListNode(data[i + 1])
            cur = cur.next
    return(head)

'''Summary: returns the length of a linked list
   Arguments: head of list
   Returns: int
   Assumptions: None
   Nothing else of interest
'''
def list_length(head):
    counter = 0
    if(head is not None and head.next is None):
        return(1)
    elif(head is not None and head.next is not None):
        while(head.next is not None):
            counter += 1
            head = head.next
    return(counter + 1)

'''Summary: Takes a linked list and splits it into 2 halves
   Arguments: head of list
   Returns: tuple with head of both new lists
   Assumptions: None
   Nothing else of interest
'''
def split_list(old_head):
    list_len = list_length(old_head)
    first_len = 0
    if(list_len % 2 == 1):
        first_len = (int(list_len / 2)) + 1
    else:
        first_len = list_len / 2
    cur = old_head
    
    for i in range(int(first_len - 1)):
        cur = cur.next
    new_head = cur.next
    cur.next = None
    return((old_head, new_head))
