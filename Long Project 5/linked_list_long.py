'''File: linked_list_long.py.
   Author: Kareem Khalidi.
   Purpose: to improve skills with linked lists
   Course: CSC 120 1st Semester.
'''

from list_node import *

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

'''Summary: returns true if list is sorted and false
            if the list is not
   Arguments: head of list
   Returns: bool
   Assumptions: None
   Nothing else of interest
'''
def is_sorted(head):
    if(head is not None and head.next is not None):
        while(head.next is not None):
            if(head.next.val < head.val):
                return(False)
            head = head.next
    return(True)

'''Summary: returns sum of vals of linked list
   Arguments: head of list
   Returns: int
   Assumptions: None
   Nothing else of interest
'''
def list_sum(head):
    sum = 0
    if(head is not None):
        if(head.next is not None):
            while(head.next is not None):
                sum += head.val
                head = head.next
            sum += head.val
        else:
            return(head.val)
    return(sum)

'''Summary: returns a tuple of lists, first one
            contains odd indexed items and second
            contains even indexed items
   Arguments: head of list
   Returns: tuple of 2 linked lists
   Assumptions: None
   Nothing else of interest
'''
def partition_list(head):
    is_even = True
    if(list_length(head) % 2 == 1):
        is_even = False
    if(head is None):
        return((head, head))
    elif(head.next is None):
        return((head, head.next))
    list1 = head
    head = head.next
    list2 = head
    head = head.next
    cur1 = list1
    cur2 = list2
    for i in range(int(list_length(head) / 2) + 1):
        if(head.next is not None):
            cur1.next = head
            head = head.next
            cur1 = cur1.next
        if(head.next is not None):
            cur2.next = head
            head = head.next
            cur2 = cur2.next
    if(is_even):
        cur2.next = cur2.next.next
        cur1.next = None
    else:
        cur1.next = cur1.next.next
        cur2.next = None
    return((list1, list2))

'''Summary: returns a list containing every 4th element
            of a list, starting at the specified element
   Arguments: head of list, int
   Returns: list
   Assumptions: None
   Nothing else of interest
'''
def accordion_4(head, start_pos):
    if(head is None):
        return(head)
    for i in range(start_pos):
        if(head.next is not None):
            head = head.next
        else:
            head = None
            return(head)
    cur = head
    while(cur.next is not None):
        if(cur.next.next is not None):
            if(cur.next.next.next is not None):
                if(cur.next.next.next.next is not None):
                    cur.next = cur.next.next.next.next
                    cur = cur.next
                else:
                    cur.next = None
                    break
            else:
                cur.next = None
                break
        else:
            cur.next = None
            break
    return(head)

'''Summary: returns the length of a linked list
   Arguments: 2 linked lists
   Returns: linked list of tuples
   Assumptions: None
   Nothing else of interest
'''
def pair(list1, list2):
    if(list1 is None or list2 is None):
        return(None)
    return_list = ListNode((list1.val, list2.val))
    list1 = list1.next
    list2 = list2.next
    return_len = list_length(list1)
    cur = return_list
    if(list_length(list2) < return_len):
        return_len = list_length(list2)
    for i in range(return_len):
        cur.next = ListNode((list1.val, list2.val))
        cur = cur.next
        list1 = list1.next
        list2 = list2.next
    return(return_list)