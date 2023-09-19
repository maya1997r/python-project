import tkinter as tk




class SmallTictactoe:
    def __init__(self):
        
        self.won = 0 # a variable to keep track if a board has won

        self.state = [[0, 0, 0],  # a list to keep track of every button state in the small board (either 1 or 2 or 0)
                      [0, 0, 0],
                      [0, 0, 0]]
        

    def reset(self): # resets every button in the small board to zero
        self.won = 0
        for i in range(3):
            for j in range(3):
                self.state[i][j] = 0
                 
    
    def check(self, current_player): # checks if a player has won a small game or not by returning the winner states which gives us the states of the board the won
 
        winner_states =[]
        
        for i in range(3):
            # check horizontal
            if (all([j == 1 for j in self.state[i]]) or 
                all([j == 2 for j in self.state[i]])):

                self.won = current_player
                for j in range(3):
                    winner_states.append([i,j])
                return winner_states

            # check vertical 
            if (self.state[0][i] == self.state[1][i] == self.state[2][i] == 1 or 
                self.state[0][i] == self.state[1][i] == self.state[2][i] == 2):

                self.won = current_player
                for j in range(3):
                    winner_states.append([j,i])
                return winner_states
            
        # Check if diagonal 1
        if (self.state[0][0] == self.state[1][1] == self.state[2][2] == 1 or
            self.state[0][0] == self.state[1][1] == self.state[2][2] == 2):

            self.won = current_player
            for j in range(3):
                winner_states.append([j, j])
            return winner_states

        # Check if diagonal 2
        if (self.state[0][2] == self.state[1][1] == self.state[2][0] == 1 or
            self.state[0][2] == self.state[1][1] == self.state[2][0] == 2):

            self.won = current_player
            for j in range(3):
                winner_states.append([j, 2 - j])
            return winner_states

        
            
        return False
    
    def update(self, row, column, current_player): # after a player clicks on a button and its valid it updates the button state and then checks if someone has won atfer each move
        if self.won == 0 and self.state[row][column] == 0 :
                self.state[row][column] = current_player
                return self.check(current_player)
            
        return None
                
            
    
    def if_full(self): # checks if a small board is full
         for i in range(3):
            for j in range(3):
                  if self.state[i][j] == 0:
                        return False
                  
         return True
    
    




    