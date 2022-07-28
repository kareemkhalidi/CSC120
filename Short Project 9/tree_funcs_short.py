'''File: tree_funcs_short.py.
   Author: Kareem Khalidi.
   Purpose: Recursive methods dealing with binary trees.
   Course: CSC 120 1st Semester.
'''

from tree_node import *

def tree_count(root):
    '''Summary: counts the num of nodes in a tree
       Arguments: root (root of the tree)
       Returns: int (amount of nodes in tree)
       Assumptions: None
       Nothing else of interest
    '''
    if root is None:
        return 0
    else:
        return 1 + tree_count(root.left) + tree_count(root.right)
    
def tree_sum(root):
    '''Summary: returns the sum of all values of the tree
       Arguments: root (root of the tree)
       Returns: int (all values in the tree summed up)
       Assumptions: all values in the tree are ints
       Nothing else of interest
    '''
    if root is None:
        return 0
    else:
        return root.val + tree_sum(root.left) + tree_sum(root.right)

def tree_depth(root):
    '''Summary: returns the depth of the tree
       Arguments: root (root of the tree)
       Returns: int (depth of the tree)
       Assumptions: None
       Nothing else of interest
    '''
    if root is None:
        return -1
    elif root.left is None and root.right is None:
        return 0
    else:
        return 1 + max(tree_depth(root.left), tree_depth(root.right))

def tree_print(root):
    '''Summary: prints out all values in the tree
       Arguments: root (root of the tree)
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''
    if root is not None:
        print(root.val)
        tree_print(root.left)
        tree_print(root.right)

def tree_build_left_linked_list(data):
    '''Summary: turns an array into a tree with only left nodes
       Arguments: array (values you want turned into a tree)
       Returns: root (root of the tree made of array values)
       Assumptions: None
       Nothing else of interest
    '''
    if len(data) == 0:
        return None
    else:
        root = TreeNode(data[0])
        root.left = tree_build_left_linked_list(data[1:])
        return root