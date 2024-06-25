from copy import copy
# Representation of the Sudoku board, domain, and constraints
class CSP:
    def __init__(self, initBoard):
        
        self.board = {}
        self.domain = {}
        self.constraints = []
        self.rows = "ABCDEFGHI"
        self.columns = "123456789"
        
        # Populate the board dictionary using nested loops
        index = 0
        for row in self.rows:
            for col in self.columns:
                key = row + col
                self.board[key] = int(initBoard[index])
                index += 1

       # Populate the domain
        domain_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in self.rows:
            for col in self.columns:
                key = row + col
                if self.board[key] == 0:  
                    self.domain[key] = domain_list.copy()
                else:
                    self.domain[key] = [int(self.board[key])] 
        
        # Populate the constraints for rows
        for row in self.rows:
            constraint = tuple(row + col for col in self.columns)
            self.constraints.append(constraint)
        
        # Populate the constraints for columns
        for col in self.columns:
            constraint = tuple(row + col for row in self.rows)
            self.constraints.append(constraint)
            
        # Populate the constraints for 3x3 quadrants
        for row_block in ('ABC', 'DEF', 'GHI'):
            for col_block in ('123', '456', '789'):
                constraint = tuple(row + col for row in row_block for col in col_block)
                self.constraints.append(constraint)
                
        #Populate neighbors
        self.neighbors = {key: [] for key in self.domain}
        
    # helper function to print the board of CSP class
    def print_board(csp):
        rows = "ABCDEFGHI"
        cols = "123456789"
        for i, r in enumerate(rows):
            if i in [3, 6]:
                print('------+-------+------'),
            for j, c in enumerate(cols):
                if j in [3, 6]:
                    print ('|', end = " "),
                print(csp.board[r + c], end=" ")
            print()