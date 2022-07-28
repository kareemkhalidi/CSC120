'''File: linked_list_long.py.
   Author: Kareem Khalidi.
   Purpose: to improve skills with linked lists
   Course: CSC 120 1st Semester.
'''


class Room:

    '''Summary: Constructor for room class
       Arguments: self, name
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, name):
        self._name = name
        self.n = None
        self.s = None
        self.e = None
        self.w = None

    '''Summary: Returns name of room
       Arguments: self
       Returns: name
       Assumptions: None
       Nothing else of interest
    '''
    def get_name(self):
        return(self._name)

    '''Summary: Sets name to new name
       Arguments: self, new_name
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def set_name(self, new_name):
        self._name = new_name

    '''Summary: Closes all entrances to the room
       Arguments: self
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def collapse_room(self):
        if(self.n is not None):
            temp = self.n
            self.n = None
            temp.s = None
        if(self.e is not None):
            temp = self.e
            self.e = None
            temp.w = None
        if(self.s is not None):
            temp = self.s
            self.s = None
            temp.n = None
        if(self.w is not None):
            temp = self.w
            self.w = None
            temp.e = None
 
'''Summary: Builds a grid of rooms of specified w and h
   Arguments: width, height
   Returns: sw_room
   Assumptions: None
   Nothing else of interest
    '''
def build_grid(width, height):
    name_count = 0
    sw_room = Room("room" + str(name_count))
    name_count += 1
    cur = sw_room
    for i in range(height - 1):
        cur.n = Room("room" + str(name_count))
        name_count += 1
        if(i is not (height - 1)):
            cur = cur.n
    cur2 = sw_room
    for i in range(width - 1):
        for j in range(height):
            cur = cur2
            cur.e = Room("room" + str(name_count))
            name_count += 1
            if(j is not height):
                cur = cur.n
            cur2 = cur2.e
    return(sw_room)