#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    """ represents a player of the Connect Four game
    """
    def __init__(self, checker):
        """ constructs a new Player object by initializing two attributes: 'checker' and 'num_moves'
            checker represents the gamepiece for the player
            num_moves stores how many moves the player has made so far, should be initialized to zero
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object. The string returned should indicate which checker
            the Player object is using.
        """
        
        s = 'Player ' + self.checker
        
        return s
        
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object's
            opponent. The method may assume that the calling Player object has a checker attribute
            that is either 'X' or 'O'
        """
        
        s = 'X'
        
        if self.checker == s:
            s = 'O'
            
        return s
    
    def next_move(self, b):
        """ accepts a Board object 'b' as a parameter and returns the column where the player wants
            to make the next move. The method should repeatedly ask for a column number until a valid column
            number is given
        """
        
        user = int(input("Enter a column: "))
        
        while b.can_add_to(user) == False:
            print("Try again!")
            user = int(input("Enter a column: "))
            
        self.num_moves += 1
        
        return user
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        