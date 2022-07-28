'''File: carcassonne_tile.py.
   Author: Kareem Khalidi.
   Purpose: Tile obj for the carcassonne game
   Course: CSC 120 1st Semester.
'''

class CarcassonneTile:
    '''Summary: CarcassonneTile class that creates a tile
                to be used in the CarcassoneMap class
       Arguments: self, n, e, s, w
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''

    def __init__(self, n, e, s, w, center=None, city_connected=False):
        '''Summary: constructor for CarcassonneTile
           Arguments: self, n, e, s, w
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        self._n = n
        self._e = e
        self._s = s
        self._w = w
        self._center = center
        self._city_connected = city_connected

    def get_edge(self, side):
        '''Summary: returns value of specified side
           Arguments: self, side
           Returns: self._side (value of side)
           Assumptions: None
           Nothing else of interest
        '''
        if side == 0:
            return self._n
        elif side == 1:
            return self._e
        elif side == 2:
            return self._s
        elif side == 3:
            return self._w

    def edge_has_road(self, side):
        '''Summary: informs user if specified side is a road
           Arguments: self, side
           Returns: true if side val = "grass+road"
                    and false otherwise
           Assumptions: None
           Nothing else of interest
        '''
        if side == 0:
            return self._n == "grass+road"
        elif side == 1:
            return self._e == "grass+road"
        elif side == 2:
            return self._s == "grass+road"
        elif side == 3:
            return self._w == "grass+road"

    def edge_has_city(self, side):
        '''Summary: informs user if specified side is a city
           Arguments: self, side
           Returns: true if side val = "city"
                    and false otherwise
           Assumptions: None
           Nothing else of interest
        '''
        if side == 0:
            return self._n == "city"
        elif side == 1:
            return self._e == "city"
        elif side == 2:
            return self._s == "city"
        elif side == 3:
            return self._w == "city"

    def has_crossroads(self):
        '''Summary: Tells user if tile has a crossroads
           Arguments: self
           Returns: True if there are 3 or more roads,
                    false if there are not
           Assumptions: None
           Nothing else of interest
        '''
        a = self._center == "crossroads"
        b = self._center == "crossroads+city"
        return a or b

    def road_get_connection(self, from_side):
        '''Summary: tells user which road the specified road is
                    connected to.
           Arguments: self, from_side
           Returns: value of other side with a road (-1 if crossroad)
           Assumptions: None
           Nothing else of interest
        '''
        if self.has_crossroads():
            return -1
        else:
            if from_side != 0 and self._n == "grass+road":
                return 0
            elif from_side != 1 and self._e == "grass+road":
                return 1
            elif from_side != 2 and self._s == "grass+road":
                return 2
            elif from_side != 3 and self._w == "grass+road":
                return 3

    def city_connects(self, sideA, sideB):
        '''Summary: informs user if specified sides are both citys and
                    connected
           Arguments: self, sideA, sideB
           Returns: true if sideA and sideB are cities with nothing
                    between them other than more cities, else False
           Assumptions: None
           Nothing else of interest
        '''
        if sideA == sideB:
            return True
        elif self.get_edge(sideB) != "city":
            return False
        elif self._city_connected:
            return True
        else:
            return False

    def rotate(self):
        '''Summary: returns current tile rotated 90 degrees
           Arguments: self
           Returns: new carcassone tile rotated 90
           Assumptions: None
           Nothing else of interest
        '''
        return CarcassonneTile(self._w, self._n, self._e, self._s, 
        center=self._center, city_connected=self._city_connected)

tile01 = CarcassonneTile("city", "grass+road", "grass", "grass+road")
tile02 = CarcassonneTile("city", "city", "grass", 
"city", center="city", city_connected=True)
tile03 = CarcassonneTile("grass+road", "grass+road",
"grass+road", "grass+road", center="crossroads+city")
tile04 = CarcassonneTile("city", "grass+road", "grass+road", "grass")
tile05 = CarcassonneTile("city", "city", "city", 
"city", center="city", city_connected=True)
tile06 = CarcassonneTile("grass+road", "grass", "grass+road", "grass")
tile07 = CarcassonneTile("grass", "city", "grass", "city")
tile08 = CarcassonneTile("grass", "city", "grass", 
"city", center="city", city_connected=True)
tile09 = CarcassonneTile("city", "city", 
"grass", "grass", city_connected=True)
tile10 = CarcassonneTile("grass", "grass+road", 
"grass+road", "grass+road", center="crossroads+city")
tile11 = CarcassonneTile("city", "grass+road", 
"grass+road", "city", city_connected=True)
tile12 = CarcassonneTile("city", "grass", "grass+road", "grass+road")
tile13 = CarcassonneTile("city", "grass+road", "grass+road", 
"grass+road", center="crossroads+city")
tile14 = CarcassonneTile("city", "city", "grass", 
"grass", city_connected=False)
tile15 = CarcassonneTile("grass", "grass", "grass+road", "grass+road")
tile16 = CarcassonneTile("city", "grass", "grass", "grass")