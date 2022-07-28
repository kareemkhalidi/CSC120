'''File: carcassonne_map.py.
   Author: Kareem Khalidi.
   Purpose: Map class for Carcassonne Game
   Course: CSC 120 1st Semester.
'''

from carcassonne_tile import *

class CarcassonneMap:
    '''Summary: CarcassonneMap class that holds the tiles
       Arguments: self
       Returns: None
       Assumptions: None
       Nothing else of interest
    '''

    def __init__(self):
        '''Summary: CarcassonneMap constructor
           Arguments: self
           Returns: None
           Assumptions: None
           Nothing else of interest
        '''
        self._tile_map = {(0, 0): tile01}

    def get_all_coords(self):
        '''Summary: returns set of all coords
           Arguments: self
           Returns: set of the _tile_map keys
           Assumptions: None
           Nothing else of interest
        '''
        return set(self._tile_map.keys())

    def find_map_border(self):
        '''Summary: returns all coords where you can put a tile
           Arguments: self
           Returns: set of all coords
           Assumptions: None
           Nothing else of interest
        '''
        r = set()
        tiles = list(self._tile_map.keys())
        for i in range(len(tiles)):
            cur = tiles[i]
            temp = (cur[0] + 1, cur[1])
            if tiles.count(temp) == 0:
                r.add(temp)
            temp = (cur[0] - 1, cur[1])
            if tiles.count(temp) == 0:
                r.add(temp)
            temp = (cur[0], cur[1] + 1)
            if tiles.count(temp) == 0:
                r.add(temp)
            temp = (cur[0], cur[1] - 1)
            if tiles.count(temp) == 0:
                r.add(temp)
        return r

    def get(self, x, y):
        '''Summary: returns tile at specified position
           Arguments: self, x, y
           Returns: CarcassonneTile at x, y
           Assumptions: None
           Nothing else of interest
        '''
        tiles = list(self._tile_map.keys())
        if tiles.count((x, y)) == 0:
            return None
        return self._tile_map[(x, y)]

    def add(self, x, y, tile, confirm=True, tryOnly=False):
        '''Summary: adds tile to map if it can be added
           Arguments: self, x, y, tile, confirm, tryOnly
           Returns: boolean indicating if tile was added
           Assumptions: None
           Nothing else of interest
        '''
        if not confirm:
            self._tile_map[(x, y)] = tile
            return True
        else:
            fits = False
            if list(self.find_map_border()).count((x, y)) > 0:
                tiles = list(self._tile_map.keys())
                closest_tiles_locations = [(x, y + 1), (x + 1, y), 
                (x, y - 1), (x - 1, y)]
                closest_tiles = []
                closest_tiles_dir = []
                for i in range(len(closest_tiles_locations)):
                    if tiles.count(closest_tiles_locations[i]) == 1:
                        closest_tiles.append(closest_tiles_locations[i])
                        closest_tiles_dir.append(i)
                for i in range(len(closest_tiles)):
                    if closest_tiles_dir[i] == 0:
                        old_tile_dir = 2
                    if closest_tiles_dir[i] == 2:
                        old_tile_dir = 0
                    if closest_tiles_dir[i] == 1:
                        old_tile_dir = 3
                    if closest_tiles_dir[i] == 3:
                        old_tile_dir = 1
                    t = self._tile_map[closest_tiles[i]].get_edge(old_tile_dir)
                    if tile.get_edge(closest_tiles_dir[i]) != t:
                        fits = False
                        break
                    else:
                        fits = True
            if fits and not tryOnly:
                self._tile_map[(x, y)] = tile
                return True
            elif fits and tryOnly:
                return True
            else:
                return False

    def trace_road_one_direction(self, x, y, side):
        '''Summary: finds path a road goes in a certain dir
           Arguments: self, x, y, side
           Returns: array of tuples representing path
           Assumptions: None
           Nothing else of interest
        '''
        r = []
        keys = list(self._tile_map.keys())
        flag = True
        while flag:
            old_side = side
            if side == 0:
                old_side = 2
            elif side == 1:
                old_side = 3
            elif side == 2:
                old_side = 0
            elif side == 3:
                old_side = 1
            if side == 0:
                y += 1
            elif side == 1:
                x += 1
            elif side == 2:
                y -= 1
            elif side == 3:
                x -= 1
            if keys.count((x, y)) == 0:
                flag = False
                break
            if self._tile_map[(x, y)].road_get_connection(old_side) == -1:
                r.append((x, y, old_side, -1))
                flag = False
                break
            else:
                r.append((x, y, old_side, 
                self._tile_map[(x, y)].road_get_connection(old_side)))
                side = self._tile_map[(x, y)].road_get_connection(old_side)
        return r

    def trace_road(self, x, y, side):
        '''Summary: traces a road in both directions
           Arguments: self, x, y, side
           Returns: array of tuples representing path
           Assumptions: None
           Nothing else of interest
        '''
        forward = self.trace_road_one_direction(x, y, side)
        backward = self.trace_road_one_direction(x, y, 
        self._tile_map[x, y].road_get_connection(side))
        backward = backward[::-1]
        for i in range(len(backward)):
            backward[i] = (backward[i][0], backward[i][1], 
            backward[i][3], backward[i][2])
        center = [(x, y, 
        self._tile_map[(x, y)].road_get_connection(side), side)]
        r = backward + center + forward
        i = len(r)
        c = 0
        while c < i:
            if r[c][2] == r[c][3]:
                r.pop(c)
                i -= 1
            else:
                c += 1
        return r

    def trace_city(self, x, y, side):
        '''Summary: traces a city and checks if its closed
           Arguments: self, x, y, side
           Returns: tuple with bool for city being closed
                    and set of tuples for all the parts of the city
           Assumptions: None
           Nothing else of interest
        '''
        complete = True
        city = {(x, y, side)}
        keep_searching = True
        while keep_searching:
            keep_searching = False
            temp = list(city)
            for i in temp:
                tile = self.get(i[0], i[1])
                if tile.city_connects(i[2], 0):
                    if temp.count((i[0], i[1], 0)) == 0:
                        city.add((i[0], i[1], 0))
                        keep_searching = True
                if tile.city_connects(i[2], 1):
                    if temp.count((i[0], i[1], 1)) == 0:
                        city.add((i[0], i[1], 1))
                        keep_searching = True
                if tile.city_connects(i[2], 2):
                    if temp.count((i[0], i[1], 2)) == 0:
                        city.add((i[0], i[1], 2))
                        keep_searching = True
                if tile.city_connects(i[2], 3):
                    if temp.count((i[0], i[1], 3)) == 0:
                        city.add((i[0], i[1], 3))
                        keep_searching = True

                opp_x = i[0]
                opp_y = i[1]
                opp_side = i[2]
                if i[2] == 0:
                    opp_side = 2
                    opp_y += 1
                elif i[2] == 1:
                    opp_side = 3
                    opp_x += 1
                elif i[2] == 2:
                    opp_side = 0
                    opp_y -= 1
                elif i[2] == 3:
                    opp_side = 1
                    opp_x -= 1
                opp_tile = self.get(opp_x, opp_y)
                if opp_tile is None:
                    complete = False
                elif opp_tile.edge_has_city(opp_side):
                    if temp.count((opp_x, opp_y, opp_side)) == 0:
                        city.add((opp_x, opp_y, opp_side))
                        keep_searching = True
        return (complete, city)
            