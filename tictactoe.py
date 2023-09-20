import tkinter as tk




class SmallTictactoe:
    def __init__(self):
        
        self.won = 0

        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        
        self.winner_cells =[]
        

    def reset(self):
        self.won = 0
        for i in range(3):
            for j in range(3):
                self.state[i][j] = 0
                 
    
    def check(self, current_player):

        
        
        for i in range(3):
            # check horizontal
            if (all([j == 1 for j in self.state[i]]) or 
                all([j == 2 for j in self.state[i]])):

                self.won = current_player
                for j in range(3):
                    self.winner_cells.append([i,j])
                return True

            # check vertical 
            if (self.state[0][i] == self.state[1][i] == self.state[2][i] == 1 or 
                self.state[0][i] == self.state[1][i] == self.state[2][i] == 2):

                self.won = current_player
                for j in range(3):
                    self.winner_cells.append([j,i])
                return True
            
        # Check if diagonal 1
        if (self.state[0][0] == self.state[1][1] == self.state[2][2] == 1 or
            self.state[0][0] == self.state[1][1] == self.state[2][2] == 2):

            self.won = current_player
            for j in range(3):
                self.winner_cells.append([j, j])
            return True

        # Check if diagonal 2
        if (self.state[0][2] == self.state[1][1] == self.state[2][0] == 1 or
            self.state[0][2] == self.state[1][1] == self.state[2][0] == 2):

            self.won = current_player
            for j in range(3):
                self.winner_cells.append([j, 2 - j])
            return True

        return False
    
    def update(self, row, column, current_player):
        if self.won == 0 and not self.is_full():
            self.state[row][column] = current_player
            self.check(current_player)
            return True
        else:
            print(f"In Small Game {row}, {column}")
            return False
                
    def is_full(self):
         for i in range(3):
            for j in range(3):
                  if self.state[i][j] == 0:
                        return False
                  
         return True
    
    




    