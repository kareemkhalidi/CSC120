'''File: annoying_recursion.py.
   Author: Kareem Khalidi.
   Purpose: to improve skills with recursion
   Course: CSC 120 1st Semester.
'''

'''Summary: returns the factorial of n
   Arguments: n
   Returns: n! (int)
   Assumptions: None
   Nothing else of interest
'''
def annoying_factorial(n):
    if(n == 0 or n == 1):
        return(1)
    elif(n == 2):
        return(2)
    elif(n == 3):
        return(6)
    elif(n == 4):
        return(4 * annoying_factorial(3))
    elif(n == 5):
        return(5 * annoying_factorial(4))
    elif(n == 6):
        return(6 * annoying_factorial(5))
    else:
        return(n * annoying_factorial(n - 1))

'''Summary: returns the fibonacci of n
   Arguments: n
   Returns: int (fibonacci of n)
   Assumptions: None
   Nothing else of interest
'''
def annoying_fibonacci(n):
    if(n == 0):
        return(0)
    elif(n == 1):
        return(1)
    elif(n == 2):
        return(1)
    elif(n == 3):
        return(2)
    elif(n == 4):
        return(annoying_fibonacci(3) + annoying_fibonacci(2))
    elif(n == 5):
        return(annoying_fibonacci(4) + annoying_fibonacci(3))
    elif(n == 6):
        return(annoying_fibonacci(5) + annoying_fibonacci(4))
    else:
        return(annoying_fibonacci(n - 1) + annoying_fibonacci(n - 2))

'''Summary: returns an array from 1 to n
   Arguments: n
   Returns: array [1, 2, ..., n]
   Assumptions: None
   Nothing else of interest
'''
def annoying_climbUp(n):
    if(n == 0):
        return([])
    elif(n == 1):
        return([1])
    elif(n == 2):
        return([1, 2])
    elif(n == 3):
        return([1, 2, 3])
    elif(n == 4):
        temp_array = annoying_climbUp(3)
        temp_array.append(4)
        return(temp_array)
    elif(n == 5):
        temp_array = annoying_climbUp(4)
        temp_array.append(5)
        return(temp_array)
    elif(n == 6):
        temp_array = annoying_climbUp(5)
        temp_array.append(6)
        return(temp_array)
    else:
        temp_array = annoying_climbUp(n - 1)
        temp_array.append(n)
        return(temp_array)

'''Summary: returns an array starting from n, 
            down to 1 and back up to n
   Arguments: n
   Returns: array [n, ..., 2, 1, 2, ..., n]
   Assumptions: None
   Nothing else of interest
'''
def annoying_climbDownUp(n):
    if(n == 0):
        return([])
    elif(n == 1):
        return([1])
    elif(n == 2):
        return([2, 1, 2])
    elif(n == 3):
        return([3, 2, 1, 2, 3])
    elif(n == 4):
        temp_array = annoying_climbDownUp(3)
        temp_array.insert(0, 4)
        temp_array.append(4)
        return(temp_array)
    elif(n == 5):
        temp_array = annoying_climbDownUp(4)
        temp_array.insert(0, 5)
        temp_array.append(5)
        return(temp_array)
    elif(n == 6):
        temp_array = annoying_climbDownUp(5)
        temp_array.insert(0, 6)
        temp_array.append(6)
        return(temp_array)
    else:
        temp_array = annoying_climbDownUp(n - 1)
        temp_array.insert(0, n)
        temp_array.append(n)
        return(temp_array)