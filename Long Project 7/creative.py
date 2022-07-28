'''File: creative.py.
   Author: Kareem Khalidi.
   Purpose: Practice with classes and callbacks
   Course: CSC 120 1st Semester.
'''

from three_shapes_game import *
import random

class Consumer:

    '''Summary: constructor for the consumer class
       Arguments: self, x, y, rad, color, right, speed
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, x, y, rad, right, up, speed):
        self._x = x
        self._y = y
        self._rad = rad
        self._right = right
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

    '''Summary: getter for the radius
       Arguments: self
       Returns: self._rad
       Assumptions: None
       Nothing else of interest
    '''
    def get_radius(self):
        return(self._rad)

    '''Summary: checks if any obj are nearby and
                removes the smaller, and gives its
                radius to the bigger obj
       Arguments: self, other, dist, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def nearby(self, other, dist, game):
        if((self._rad / 2) + (other._rad / 2) >= dist and 
        self._rad > other._rad):
                self._rad += other._rad
                game.remove_obj(other)

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

    '''Summary: if an obj has rad 400 or more removes 
                the obj and increases the score by 1
       Arguments: self, game
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def test_score(self, game):
        if(self._rad >= 400):
            game.remove_obj(self)
            global score
            score += 1

    '''Summary: creates the obj in the window
       Arguments: self, win
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def draw(self, win):
        win.text(10, 10, str(score), "black")
        win.ellipse(self._x, self._y, self._rad, self._rad, "black")
        if(self._rad < 100):
            win.text(self._x - int(self._rad / 2.5), 
            self._y - int(self._rad / 2.5), str(self._rad), 
            "white", int(self._rad / 2))
        else:
            win.text(self._x - int(self._rad / 3), 
            self._y - int(self._rad / 3), str(self._rad), 
            "white", int(self._rad / 3))

'''Summary: creates a consumer obj with random parameters
   Arguments: game, wid, hei
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def spawn_consumer(game, wid, hei):
    x = random.randint(0, wid)
    y = random.randint(0, hei)
    rad = random.randint(10, 50)
    dir_rand = random.randint(0, 1)
    if(dir_rand == 0):
        right = True
    else:
        right = False
    dir_rand = random.randint(0, 1)
    if(dir_rand == 0):
        up = True
    else:
        up = False
    speed = random.randint(1, 5)
    game.add_obj(Consumer(x, y, rad, right, up, speed))

'''Summary: main method where all functions are called
            and all obj are created
   Arguments: none
   Returns: nothing
   Assumptions: None
   Nothing else of interest
'''
def main():
    wid = 800
    hei = 800

    game = Game("Three Shapes", 30, wid, hei)
    
    counter = 0

    global score
    score = 0

    while not game.is_over():
        counter += 1
        if(counter == 30):
            counter = 0
            spawn_consumer(game, wid, hei) 

        game.do_score_calls()
        game.do_nearby_calls()
        game.do_move_calls()
        game.do_edge_calls()
        game.draw()

if __name__ == "__main__":
    main()