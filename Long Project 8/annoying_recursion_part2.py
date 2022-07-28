'''File: annying_recursion_part2.py.
   Author: Kareem Khalidi.
   Purpose: Practice with recursion
   Course: CSC 120 1st Semester.
'''

'''Summary: returns the triangle sum of n
   Arguments: n
   Returns: int
   Assumptions: None
   Nothing else of interest
'''
def annoying_triangleNumbers(n):
    if(n == 0):
        return(0)
    elif(n == 1):
        return(1)
    elif(n == 2):
        return(3)
    elif(n == 3):
        return(6)
    elif(n == 4):
        return(4 + annoying_triangleNumbers(3))
    elif(n == 5):
        return(5 + annoying_triangleNumbers(4))
    elif(n == 6):
        return(6 + annoying_triangleNumbers(5))
    else:
        return(n + annoying_triangleNumbers(n - 1))

'''Summary: returns the first n values of the fibonacci sequence
   Arguments: n
   Returns: array
   Assumptions: None
   Nothing else of interest
'''
def annoying_fibonacci_sequence(n):
    if(n == 0):
        return([])
    elif(n == 1):
        return([0])
    elif(n == 2):
        return([0, 1])
    elif(n == 3):
        return([0, 1, 1])
    elif(n == 4):
        temp = annoying_fibonacci_sequence(3)
        temp.append(temp[-1] + temp[-2])
        return(temp)
    elif(n == 5):
        temp = annoying_fibonacci_sequence(4)
        temp.append(temp[-1] + temp[-2])
        return(temp)
    elif(n == 6):
        temp = annoying_fibonacci_sequence(5)
        temp.append(temp[-1] + temp[-2])
        return(temp)
    else:
        temp = annoying_fibonacci_sequence(n - 1)
        temp.append(temp[-1] + temp[-2])
        return(temp)

'''Summary: prints out an image of a valley resized to n
   Arguments: n
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def annoying_valley(n):
    if(n == 0):
        n = 0
    elif(n == 1):
        print("*")
    elif(n == 2):
        print("./")
        print("*")
        print(".\\")
    elif(n == 3):
        print("../")
        print("./")
        print("*")
        print(".\\")
        print("..\\")
    elif(n == 4):
        print((3 * ".") + "/")
        annoying_valley(3)
        print((3 * ".") + "\\")
    elif(n == 5):
        print((4 * ".") + "/")
        annoying_valley(4)
        print((4 * ".") + "\\")
    elif(n == 6):
        print((5 * ".") + "/")
        annoying_valley(5)
        print((5 * ".") + "\\")
    else:
        print(((n - 1) * ".") + "/")
        annoying_valley(n - 1)
        print(((n - 1) * ".") + "\\")