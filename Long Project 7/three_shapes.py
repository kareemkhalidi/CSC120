'''File: three_shapes.py.
   Author: Kareem Khalidi.
   Purpose: Practice with classes and callbacks
   Course: CSC 120 1st Semester.
'''

from three_shapes_game import *
import random

class Circle:

    '''Summary: constructor for the circle class
       Arguments: self, x, y, rad, color, right, speed
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, x, y, rad, color, right, speed):
        self._x = x
        self._y = y
        self._rad = rad
        self._color = color
        self._right = right
        self._speed = speed

    '''Summary: getter for the position
       Arguments: self
       Returns: tuple(self._x, self._y)
       Assumptions: None
       Nothing else of interest
    '''
    def get_xy(self):
        return((self._x, self._y))

    '''Summary: getter for the radios
       Arguments: self
       Returns: self._rad
       Assumptions: None
       Nothing else of interest
    '''
    def get_radius(self):
        return(self._rad)

    '''Summary: getter for the classes shape
       Arguments: self
       Returns: "circle"
       Assumptions: None
       Nothing else of interest
    '''
    def get_shape(self):
        return("circle")

    '''Summary: checks if any obj are nearby and
                removes one of them based on specs
                provided
       Arguments: self, other, dist, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def nearby(self, other, dist, game):
        if((self._rad / 2) + (other._rad / 2) >= dist):
            if(self.get_shape() == "circle" and
             other.get_shape() == "square"):
                game.remove_obj(self)
            elif(self.get_shape() == "circle" and
             other.get_shape() == "triangle"):
                game.remove_obj(other)
            elif(self.get_shape() == "square" and
             other.get_shape() == "triangle"):
                game.remove_obj(self)

    '''Summary: checks if the obj is near the edge
                and reverses its direction if it is
       Arguments: self, dir, position
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def edge(self, dir, position):
        if(dir == "right"):
            self._right = False
        elif(dir == "left"):
            self._right = True

    '''Summary: moves the obj based on its 
                dir(right) and speed
       Arguments: self, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def move(self, game):
        if(self._right):
            self._x += self._speed
        else:
            self._x -= self._speed

    '''Summary: creates the obj in the window
       Arguments: self, win
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def draw(self, win):
        win.ellipse(self._x, self._y, self._rad, self._rad, self._color)

class Square:

    '''Summary: constructor for the square class
       Arguments: self, x, y, rad, color, up, speed
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, x, y, rad, color, up, speed):
        self._x = x
        self._y = y
        self._rad = rad
        self._color = color
        self._up = up
        self._speed = speed

    '''Summary: getter for the position
       Arguments: self
       Returns: tuple(self._x, self._y)
       Assumptions: None
       Nothing else of interest
    '''
    def get_xy(self):
        return((self._x, self._y))

    '''Summary: getter for the radios
       Arguments: self
       Returns: self._rad
       Assumptions: None
       Nothing else of interest
    '''
    def get_radius(self):
        return(self._rad)

    '''Summary: getter for the classes shape
       Arguments: self
       Returns: "square"
       Assumptions: None
       Nothing else of interest
    '''
    def get_shape(self):
        return("square")

    '''Summary: checks if any obj are nearby and
                removes one of them based on specs
                provided
       Arguments: self, other, dist, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def nearby(self, other, dist, game):
        if((self._rad / 2) + (other._rad / 2) >= dist):
            if(self.get_shape() == "circle" and 
            other.get_shape() == "square"):
                game.remove_obj(self)
            elif(self.get_shape() == "circle" and 
            other.get_shape() == "triangle"):
                game.remove_obj(other)
            elif(self.get_shape() == "square" and 
            other.get_shape() == "triangle"):
                game.remove_obj(self)

    '''Summary: checks if the obj is near the edge
                and reverses its direction if it is
       Arguments: self, dir, position
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def edge(self, dir, position):
        if(dir == "top"):
            self._up = True
        elif(dir == "bottom"):
            self._up = False

    '''Summary: moves the obj based on its 
                dir(up) and speed
       Arguments: self, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def move(self, game):
        if(self._up):
            self._y += self._speed
        else:
            self._y -= self._speed

    '''Summary: creates the obj in the window
       Arguments: self, win
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''  
    def draw(self, win):
        win.rectangle(self._x, self._y, self._rad, self._rad, self._color)

class Triangle:

    '''Summary: constructor for the circle class
       Arguments: self, x, y, rad, color, up, right, speed
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, x, y, rad, color, up, right, speed):
        self._x = x
        self._y = y
        self._rad = rad
        self._color = color
        self._up = up
        self._right = right
        self._speed = speed

    '''Summary: getter for the position
       Arguments: self
       Returns: tuple(self._x, self._y)
       Assumptions: None
       Nothing else of interest
    '''
    def get_xy(self):
        return((self._x, self._y))

    '''Summary: getter for the radios
       Arguments: self
       Returns: self._rad
       Assumptions: None
       Nothing else of interest
    '''
    def get_radius(self):
        return(self._rad)

    '''Summary: getter for the classes shape
       Arguments: self
       Returns: "triangle"
       Assumptions: None
       Nothing else of interest
    '''
    def get_shape(self):
        return("triangle")

    '''Summary: checks if any obj are nearby and
                removes one of them based on specs
                provided
       Arguments: self, other, dist, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def nearby(self, other, dist, game):
        if((self._rad / 2) + (other._rad / 2) >= dist):
            if(self.get_shape() == "circle" and 
            other.get_shape() == "square"):
                game.remove_obj(self)
            elif(self.get_shape() == "circle" and 
            other.get_shape() == "triangle"):
                game.remove_obj(other)
            elif(self.get_shape() == "square" and 
            other.get_shape() == "triangle"):
                game.remove_obj(self)

    '''Summary: checks if the obj is near the edge
                and reverses its direction if it is
       Arguments: self, dir, position
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def edge(self, dir, position):
        if(dir == "top"):
            self._up = True
        elif(dir == "bottom"):
            self._up = False
        
        if(dir == "right"):
            self._right = False
        elif(dir == "left"):
            self._right = True

    '''Summary: moves the obj based on its 
                dir(right and up) and speed
       Arguments: self, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def move(self, game):
        if(self._up):
            self._y += self._speed
        else:
            self._y -= self._speed
        
        if(self._right):
            self._x += self._speed
        else:
            self._x -= self._speed

    '''Summary: creates the obj in the window
       Arguments: self, win
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''  
    def draw(self, win):
        win.triangle(self._x, self._y, self._x - self._rad, 
        self._y + (2 * self._rad), self._x + self._rad, 
        self._y + (2 * self._rad), self._color)

'''Summary: creates a circle obj with random parameters
   Arguments: game, wid, hei
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def spawn_circle(game, wid, hei):
    x = random.randint(0, wid)
    y = random.randint(0, hei)
    rad = random.randint(10, 50)
    color_rand = random.randint(0, 2)
    if(color_rand == 0):
        color = "red"
    elif(color_rand == 1):
        color = "green"
    else:
        color = "blue"
    dir_rand = random.randint(0, 1)
    if(dir_rand == 0):
        right = True
    else:
        right = False
    speed = random.randint(1, 5)
    game.add_obj(Circle(x, y, rad, color, right, speed))

'''Summary: creates a square obj with random parameters
   Arguments: game, wid, hei
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def spawn_square(game, wid, hei):
    x = random.randint(0, wid)
    y = random.randint(0, hei)
    rad = random.randint(10, 50)
    color_rand = random.randint(0, 2)
    if(color_rand == 0):
        color = "red"
    elif(color_rand == 1):
        color = "green"
    else:
        color = "blue"
    dir_rand = random.randint(0, 1)
    if(dir_rand == 0):
        up = True
    else:
        up = False
    speed = random.randint(1, 5)
    game.add_obj(Square(x, y, rad, color, up, speed))

'''Summary: creates a triangle obj with random parameters
   Arguments: game, wid, hei
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def spawn_triangle(game, wid, hei):
    x = random.randint(0, wid)
    y = random.randint(0, hei)
    rad = random.randint(5, 25)
    color_rand = random.randint(0, 2)
    if(color_rand == 0):
        color = "red"
    elif(color_rand == 1):
        color = "green"
    else:
        color = "blue"
    dir_rand = random.randint(0, 1)
    if(dir_rand == 0):
        up = True
    else:
        up = False
    dir_rand = random.randint(0, 1)
    if(dir_rand == 0):
        right = True
    else:
        right = False
    speed = random.randint(1, 5)
    game.add_obj(Triangle(x, y, rad, color, up, right, speed))

'''Summary: constructor for the circle class
   Arguments: self, x, y, rad, color, right, speed
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def main():
    wid = 500
    hei = 500

    game = Game("Three Shapes", 30, wid, hei)
    
    counter = 0

    while not game.is_over():
        counter += 1
        if(counter == 30):
            counter = 0
            current_shape = random.randint(1, 3)
            if(current_shape == 1):
                spawn_circle(game, wid, hei)
            elif(current_shape == 2):
                spawn_square(game, wid, hei)
            else:
                spawn_triangle(game, wid, hei)
        
        game.do_nearby_calls()
        game.do_move_calls()
        game.do_edge_calls()
        game.draw()

if __name__ == "__main__":
    main()