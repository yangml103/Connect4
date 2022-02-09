#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ AI Player
    """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ returns a string representing an AIPlayer object, this will overrode 
            the __repr__ method inherited from Player
        """ 
        
        p = 'Player ' + str(self.checker) + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        
        return p
    
    def max_score_column(self, scores):
        """ takes a list of scores containing a score for each column of the board, and returns
            the index of the column with the maximum score. if one or more columns are tied for the maximum score
            the method should apply the tiebreaking strategy
        """
        
        largest = max(scores)
        new_list = []
        
        for i in range(len(scores)):
            if largest == scores[i]:
                new_list += [i]
        if self.tiebreak == 'RIGHT':
            return new_list[-1]
        
        elif self.tiebreak == 'LEFT':
            return new_list[0]
        
        else:
            return random.choice(new_list)
        
    def scores_for(self, b):
        """ takes a board object 'b' and determines the AIPlayer's scores for each column
            based on the lookahead value. the method should return a list containing one score for each column
        """
        scores = [-1]*b.width
       
        for i in range(b.width):
           
            if b.can_add_to(i) == False:
                scores[i] = -1
                
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
                
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
                
            elif self.lookahead == 0:
                scores[i] = 50
                
            else:
                b.add_checker(self.checker, i)
                
                s = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                
                
                
                scores2 = s.scores_for(b)
                
               
               
                if max(scores2) == 0:
                    scores[i] = 100
                elif max(scores2) == 50:
                    scores[i] = 50
                        
                else:
                    scores[i] = 0
                    
               
                b.remove_checker(i)
                
        
        return scores
    
    def next_move(self, b):
        """ overrides the inherited next_move method, this version should return the 
            called AIPlayer's judgement of its best possible move. It should also 
            increment the number of moves that the AIPlayer object has made.
        """
        
        x = self.max_score_column(self.scores_for(b))
        self.num_moves += 1 
        return x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        