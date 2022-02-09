#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        
        s += '-' * (self.width*2 + 1)
        s += '\n'
        
        count = 0
        for x in range(self.width):
            if count < 10:
                s += ' ' + str(count)
                count += 1
            else:
                count = 0 
                s += ' ' + str(count)
                count += 1
    
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = 0
        
        while row < self.height and self.slots[row][col] == ' ':
            row += 1
            
        self.slots[row-1][col] = checker
        

    
    ### add your reset method here ###
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def reset(self):
        """ resets the Board object on which it is called by setting all slots to 
            contain a space character
        """
        
        self.slots = [[' '] * self.width for row in range(self.height)]
        
        
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column 'col'
            otherwise, it should return False
        """
        
        if col >= self.width or col < 0:
            return False
        
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
        
    def is_full(self):
        """ returns True if the called Board object is completely full of checkers and False otherwise
        """
        for i in range(self.width):
            if self.can_add_to(i) == True:
                return False
            
        return True
        
    def remove_checker(self, col):
        """ removes the top checker from column 'col' of the Board object. If the column is empty, then 
            the method should do nothing
        """
        row = 0 
       
        while row < self.height and self.slots[row][col] == ' ':
            row +=1
            
        if row < self.height and self.slots[row][col] != ' ':
            
            self.slots[row][col] = ' '
            
            
    def is_win_for(self, checker):
        """ accepts a parameter 'checker' that is either 'X' or 'O' and returns Trus if there are four
            consecutive slots containing 'checker' on the board. Otherwise, it should return False
        """
        assert(checker == 'X' or checker == 'O')
            
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and self.slots[row][col+1] == checker and self.slots[row][col+2] == checker and self.slots[row][col+3] == checker:
                    # horizontal check 
                    return True
                
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and self.slots[row+1][col] == checker and self.slots[row+2][col] == checker and self.slots[row+3][col] == checker:
                    # vertical check
                    return True
                
        for row in range(self.height//2,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and self.slots[row-1][col+1] == checker and self.slots[row-2][col+2] == checker and self.slots[row-3][col+3] == checker:
                    # diagonal bottom left to top right check
                    return True
                
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and self.slots[row+1][col+1] == checker and self.slots[row+2][col+2] == checker and self.slots[row+3][col+3] == checker:
                    return True
                
        return False
    
                
                                   
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
