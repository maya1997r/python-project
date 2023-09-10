import tkinter as tk




class Tictactoe:
    def __init__(self, frame):
        
        self.done = False

        


        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        

          

    


    def reset(self):
        self.done = False
        for i in range(3):
            for j in range(3):
                
                 self.state[i][j] = 0
                 
    
    def check(self):

        winner_states =[]
        
        for i in range(3):
            # check if horizontal
            if (all([j == 1 for j in self.state[i]])):
                self.done = True
                for j in range(3):

                    winner_states.append([i,j])
                return winner_states

            elif (all([j == 2 for j in self.state[i]])):
                self.done = True
                for j in range(3):
                    winner_states.append([i,j])
                return winner_states

            # check if vertical 
            if (self.state[0][i] == self.state[1][i] == self.state[2][i] == 1):
                self.done = True
                for j in range(3):
                    
                    winner_states.append([j,i])
                return winner_states

            elif (self.state[0][i] == self.state[1][i] == self.state[2][i] == 2):
                self.done = True
                for j in range(3):
                    winner_states.append([j,i])
                return winner_states

        #check if diagonal 1
        if (self.state[0][0] == self.state[1][1] == self.state[2][2] == 1):
            self.done = True
            for j in range(3):
                winner_states.append([j,j])
                return winner_states

        elif (self.state[0][0] == self.state[1][1] == self.state[2][2] == 2):
            self.done = True
            for j in range(3):
                winner_states.append([j,j])
                return winner_states

        
        #check if diagonal 2
        if (self.state[0][2] == self.state[1][1] == self.state[2][0] == 1):
            self.done = True
            for j in range(3):
                winner_states.append([j,j])
                return winner_states

        elif (self.state[0][2] == self.state[1][1] == self.state[2][0] == 2):
            self.done = True
            for j in range(3):
                winner_states.append([j,2-j])
                return winner_states

        elif self.if_full() == True:
            self.done = True
            for i in range(3):
                for j in range(3):
                    winner_states.append([i,j])
                return winner_states
            
        return True
    
    def update(self, row, column, current_player):
        if not self.done:
            if self.state[row][column] == 0 :
                self.state[row][column] = current_player
                return self.check()
            
        return None
                
            
    
    def if_full(self):
         for i in range(3):
            for j in range(3):
                  if self.state[i][j] == 0:
                        return False
                  
         return True
    
    




    