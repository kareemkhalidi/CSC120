'''File: shapes.py.
   Author: Kareem Khalidi.
   Purpose: to create code that returns certain reference diagrams.
   Course: CSC 120 1st Semester.
'''

'''Summary: Returns an array that represents a reference diagram.
   Arguments: None.
   Returns: Array.
   Assumptions: None.
   Nothing else of interest.
'''
def shape_alpha():
    return_array = [[10, 20], 30, 40, [50, 60]]
    return(return_array)

'''Summary: Returns an array that represents a reference diagram.
   Arguments: None.
   Returns: Array.
   Assumptions: None.
   Nothing else of interest.
'''
def shape_bravo():
    array1 = [123, 456]
    array2 = [789, 1024]
    return_array = [[array1, array2], [array2, array1]]
    return(return_array)

'''Summary: Returns an array that represents a reference diagram, 
            where the array stores whatever arg1 is passed.
   Arguments: arg1, can be any value as long as it can be stored 
              in an array.
   Returns: Array.
   Assumptions: arg1 can be stored in an array/list
   Nothing else of interest.
'''
def shape_charlie(arg1):
    return_array = [[[arg1, arg1], [arg1, arg1]], [arg1, arg1]]
    return(return_array)

'''Summary: Returns an array that represents a reference diagram,
            where the values stored can be changed by passing 
            arg1 and arg2
   Arguments: arg1 and arg2, any values that can be stored in
              an array.
   Returns: Array.
   Assumptions: arg1 and arg 2 can be stored in an array.
   Nothing else of interest.
'''
def shape_delta(arg1, arg2):
    return_array = [arg1, arg2, [[arg1, [arg2]], [arg1]], [17]]
    return(return_array)

'''Summary: Returns an array that represents a reference diagram
            where the values stored are represented by arg1, arg2
            and arg3. The array references itself.
   Arguments: arg1, arg2, arg3, which can be any values as long as
              they can be stored in an array.
   Returns: Recursive array.
   Assumptions: Arg1, arg2, and arg3 can be stored in an array
   Nothing else of interest.
'''
def shape_echo(arg1, arg2, arg3):
    array1 = [arg1]
    array2 = [arg2]
    array3 = [arg3]
    array1.append(array2)
    array2.append(array3)
    array3.append(array1)
    return(array1)