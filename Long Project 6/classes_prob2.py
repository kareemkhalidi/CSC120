'''File: linked_list_long.py.
   Author: Kareem Khalidi.
   Purpose: to improve skills with linked lists
   Course: CSC 120 1st Semester.
'''

class Color:

    '''Summary: Constructor for the color class
       Arguments: self, r, g, b
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, r, g, b):
        self.__r = self.constrain_bounds(r)
        self.__g = self.constrain_bounds(g)
        self.__b = self.constrain_bounds(b)

    '''Summary: Sets value specified to 255 if its
                greater than 255 and 0 if less than 0
       Arguments: self, value
       Returns: constrained value
       Assumptions: None
       Nothing else of interest
    '''
    def constrain_bounds(self, value):
        if(value >= 255):
            return(255)
        elif(value <= 0):
            return(0)
        else:
            return(value)

    '''Summary: Returns the rgb in a string form
       Arguments: self
       Returns: string containing r, g, and b
       Assumptions: None
       Nothing else of interest
    '''
    def __str__(self):
        return("rgb({},{},{})".format(self.__r, self.__g, self.__b))

    '''Summary: Returns hex verion of the rgb value
       Arguments: self
       Returns: hex string of r, g, and b
       Assumptions: None
       Nothing else of interest
    '''
    def html_hex_color(self):
        r_hex = str(hex(self.__r))[2:].upper()
        g_hex = str(hex(self.__g))[2:].upper()
        b_hex = str(hex(self.__b))[2:].upper()
        if(len(r_hex) == 1):
            r_hex = "0" + r_hex
        if(len(g_hex) == 1):
            g_hex = "0" + g_hex
        if(len(b_hex) == 1):
            b_hex = "0" + b_hex
        return("#{}{}{}".format(r_hex, g_hex, b_hex))

    '''Summary: Returns tuple of the r g b values
       Arguments: self
       Returns: tuple(r, g, b)
       Assumptions: None
       Nothing else of interest
    '''
    def get_rgb(self):
        return((self.__r, self.__g, self.__b))

    '''Summary: Sets basic colors
       Arguments: self, name
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def set_standard_color(self, name):
        if(name.lower() == "red"):
            self.__r = 255
            self.__g = 0
            self.__b = 0
        elif(name.lower() == "yellow"):
            self.__r = 255
            self.__g = 255
            self.__b = 0
        elif(name.lower() == "white"):
            self.__r = 255
            self.__g = 255
            self.__b = 255
        elif(name.lower() == "black"):
            self.__r = 0
            self.__g = 0
            self.__b = 0

    '''Summary: Sets red to 0
       Arguments: self
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def remove_red(self):
        self.__r = 0