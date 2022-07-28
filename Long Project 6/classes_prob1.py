'''File: classes_prob1.py.
   Author: Kareem Khalidi.
   Purpose: Improve knowledge of classes
   Course: CSC 120 1st Semester.
'''

class Simplest:

    '''Summary: constructor for the simplest class
       Arguments: self, a, b, c
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:

    '''Summary: Constructor for the Rotate class
       Arguments: self, first, second, third
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    '''Summary: Returns the value of first
       Arguments: self
       Returns: first
       Assumptions: None
       Nothing else of interest
    '''
    def get_first(self):
        return(self.first)

    '''Summary: Returns the value of second
       Arguments: self
       Returns: second
       Assumptions: None
       Nothing else of interest
    '''
    def get_second(self):
        return(self.second)

    '''Summary: Returns the value of third
       Arguments: self
       Returns: third
       Assumptions: None
       Nothing else of interest
    '''
    def get_third(self):
        return(self.third)

    '''Summary: Rotates the lists values, so a = b,
                b = c, and c = a
       Arguments: self
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def rotate(self):
        temp = self.first
        self.first = self.second
        self.second = self.third
        self.third = temp

class Band:

    '''Summary: Constructor for band class
       Arguments: self, singer
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def __init__(self, singer):
        self.singer = singer
        self.drummer = None
        self.guitar_players = []

    '''Summary: Returns value of singer
       Arguments: self
       Returns: singer
       Assumptions: None
       Nothing else of interest
    '''
    def get_singer(self):
        return(self.singer)

    '''Summary: Sets value of singer to specified val
       Arguments: self, new_singer
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def set_singer(self, new_singer):
        self.singer = new_singer

    '''Summary: Returns value of drummer
       Arguments: self
       Returns: drummer
       Assumptions: None
       Nothing else of interest
    '''
    def get_drummer(self):
        return(self.drummer)

    '''Summary: Sets value of drummer to specified val
       Arguments: self, new_drummer
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def set_drummer(self, new_drummer):
        self.drummer = new_drummer

    '''Summary: Adds guitar player to the list
       Arguments: self, new_guitar_player
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def add_guitar_player(self, new_guitar_player):
        self.guitar_players.append(new_guitar_player)

    '''Summary: Clears guitar_players list
       Arguments: self
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def fire_all_guitar_players(self):
        self.guitar_players = []

    '''Summary: Returns a copy of the guitar_players list
       Arguments: self
       Returns: copy of guitar_players
       Assumptions: None
       Nothing else of interest
    '''
    def get_guitar_players(self):
        copy = []
        for i in range(len(self.guitar_players)):
            copy.append(self.guitar_players[i])
        return(copy)

    '''Summary: Plays music based on the band members
       Arguments: self
       Returns: nothing
       Assumptions: None
       Nothing else of interest
    '''
    def play_music(self):
        if(self.singer == "Frank Sinatra"):
            print("Do be do be do")
        elif(self.singer == "Kurt Cobain"):
            print("bargle nawdle zouss")
        else:
            print("La la la")
        
        if(self.drummer is not None):
            print("Bang bang bang!")
        
        for i in range(len(self.guitar_players)):
            print("Strum!")