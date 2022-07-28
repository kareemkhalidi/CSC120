'''File: battleship.py.
   Author: Kareem Khalidi.
   Purpose: Battleship Game.
   Course: CSC 120 1st Semester.
'''

class Board:
    '''Summary: Board class on which the game is played
       Arguments: N/A
       Returns: N/A
       Assumptions: N/A
       Nothing else of interest
    '''

    def __init__(self, size):
        '''Summary: Board constuctor
           Arguments: self, size
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        assert size > 0
        self._size = size
        self._hits = []
        self._ships = []

    def add_ship(self, ship, position):
        '''Summary: Adds ship to the board
           Arguments: self, ship, position
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        shifted_locations = []
        for i in ship.get_shape():
            new_x = i[0] + position[0]
            new_y = i[1] + position[1]
            assert new_x >= 0 and new_x < self._size
            assert new_y >= 0 and new_y < self._size
            for j in self._ships:
                assert j.get_shape().count((new_x, new_y)) == 0
            shifted_locations.append((new_x, new_y))
        ship.update_pos(shifted_locations)
        self._ships.append(ship)

    def print(self):
        '''Summary: Prints the game board
           Arguments: self
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        if self._size > 10:
            h_edge = "   +"
        else:
            h_edge = "  +"
        for i in range(self._size):
            h_edge += "--"
        h_edge += "-+"
        print(h_edge)
        for i in range(self._size):
            cur_line = cur_line = str(self._size - i - 1) + " | "
            for j in range(self._size):
                cur_location = (j, self._size - i - 1)
                ship_at_cur = False
                for k in self._ships:
                    if k.get_shape().count(cur_location) > 0:
                        ship_at_cur = k
                if not ship_at_cur:
                    if self._hits.count(cur_location) > 0:
                        cur_line += "o "
                    else:
                        cur_line += ". "
                else:
                    if ship_at_cur.is_sunk():
                        cur_line += "X "
                    elif self._hits.count(cur_location) > 0:
                        cur_line += "* "
                    else:
                        cur_line += ship_at_cur.get_name()[0] + " "
            cur_line += "|"
            if self._size >= 11:
                if self._size - i - 1 >= 10:
                    print(cur_line)
                else:
                    print(" " + cur_line)
            else:
                print(cur_line)
        print(h_edge)
        if self._size > 10:
            cur_line = "                         "
            for i in range(self._size - 10):
                cur_line += str(i + 10)[0] + " "
            print(cur_line)
        cur_line = "     "
        for i in range(self._size):
            if i < 10:
                cur_line += str(i) + " "
            else:
                cur_line += str(i)[1] + " "
        print(cur_line)

    def has_been_used(self, position):
        '''Summary: Checks if a certain location has been
                    hit yet
           Arguments: self, position
           Returns: Boolean representing hit or not
           Assumptions: None
           Nothing else of interest
        '''
        return self._hits.count(position) > 0

    def attempt_move(self, position):
        '''Summary: makes a move on the board (fires shot)
           Arguments: self, position
           Returns: String representing success/failure
           Assumptions: None
           Nothing else of interest
        '''
        assert position[0] >= 0 and position[0] < self._size
        assert position[1] >= 0 and position[1] < self._size
        assert not self.has_been_used(position)
        self._hits.append(position)
        for i in self._ships:
            if i.get_shape().count(position) > 0:
                i.hit_ship(position)
                if i.is_sunk():
                    return("Sunk (" + i.get_name() + ")")
                return("Hit")
        return("Miss")      

class Ship:
    '''Summary: Ship class
       Arguments: N/A
       Returns: N/A
       Assumptions: N/A
       Nothing else of interest
    '''

    def __init__(self, name, shape):
        '''Summary: Ship constructor
           Arguments: self, name, shape
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        self._name = name
        self._shape = shape
        self._hits = []

    def get_name(self):
        '''Summary: Returns the ships name
           Arguments: self
           Returns: name of ship (string)
           Assumptions: None
           Nothing else of interest
        '''
        return self._name

    def get_shape(self):
        '''Summary: Returns the ships shape
           Arguments: self
           Returns: shape of ship (array of tuples)
           Assumptions: None
           Nothing else of interest
        '''
        return self._shape

    def hit_ship(self, position):
        '''Summary: applies a hit onto the ship
           Arguments: self, position
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        self._hits.append(position)

    def update_pos(self, position):
        '''Summary: Updates the ships position
           Arguments: self, position
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        self._shape = position

    def print(self):
        '''Summary: Prints the ship
           Arguments: self
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        r = ""
        for i in self._shape:
            if self._hits.count(i) > 0:
                r += "*"
            else:
                r += self.get_name()[0]
        while len(r) < 10:
            r += " "
        print(r + self._name)

    def is_sunk(self):
        '''Summary: Checks if the ship is sunk
           Arguments: self
           Returns: boolean representing if the ship is sunk
           Assumptions: None
           Nothing else of interest
        '''
        shape = self._shape.copy()
        hits = self._hits.copy()
        shape.sort()
        hits.sort()
        return shape == hits

    def rotate(self, amount):
        '''Summary: rotates the ship
           Arguments: self
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        assert amount >= 0 and amount <= 3
        new_shape = []
        for i in self._shape:
            x = i[0]
            y = i[1]
            for j in range(amount):
                temp = x * -1
                x = y
                y = temp
            new_shape.append((x, y))
        self._shape = new_shape