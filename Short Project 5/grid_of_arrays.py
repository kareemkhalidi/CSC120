'''File: grid_of_arrays.py.
   Author: Kareem Khalidi.
   Purpose: 1 method that returns a certain grid of arrays
   Course: CSC 120 1st Semester.
'''

import list_node

'''Summary: Returns a grid of arrays that represent a reference diagram.
   Arguments: None.
   Returns: Array.
   Assumptions: None.
   Nothing else of interest.
'''
def grid_of_arrays():
    array9 = [None, (2, 2), None]
    array8 = [array9, (1, 2), None]
    array7 = [array8, (0, 2), None]
    array6 = [None, (2, 1), array9]
    array5 = [array6, (1, 1), array8]
    array4 = [array5, (0, 1), array7]
    array3 = [None, (2, 0), array6]
    array2 = [array3, (1, 0), array5]
    array1 = [array2, (0, 0), array4]
    return(array1)

