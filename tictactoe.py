import tkinter as tk




class Tictactoe:
    def __init__(self, frame, font):
        
        self.done = False
        self.current_player = "X"

        self.empty_button = "    "

        self.font = font

        self.state = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        
        self.buttons = []

        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                button = tk.Button(frame, text = self.empty_button, 
                                   font = self.font, 
                                   command = lambda i=i, j=j: self.button_click(i, j))
                
                button.grid(row=i , column = j, sticky='EWNS')
                self.buttons[i].append(button)

          

          


    def reset(self):
        self.done = False
        for i in range(3):
            for j in range(3):
                #  self.buttons[i][j]["text"] = 
                 self.buttons[i][j].config(text= self.empty_button,
                                           bg=None)
                 self.state[i][j] = 0
    
    def check(self):
        for i in range(3):
            # check if horizontal
            if (all([j == 1 for j in self.state[i]])):
                self.done = True
                for j in range(3):
                    self.buttons[i][j].config(bg="red")

            elif (all([j == 2 for j in self.state[i]])):
                self.done = True
                for j in range(3):
                    self.buttons[i][j].config(bg="green")

            # check if vertical 
            if (self.state[0][i] == self.state[1][i] == self.state[2][i] == 1):
                self.done = True
                for j in range(3):
                    self.buttons[j][i].config(bg="red")

            elif (self.state[0][i] == self.state[1][i] == self.state[2][i] == 2):
                self.done = True
                for j in range(3):
                    self.buttons[j][i].config(bg="green")

        #check if diagonal 1
        if (self.state[0][0] == self.state[1][1] == self.state[2][2] == 1):
            self.done = True
            for j in range(3):
                self.buttons[j][j].config(bg="red")

        elif (self.state[0][0] == self.state[1][1] == self.state[2][2] == 2):
            self.done = True
            for j in range(3):
                self.buttons[j][j].config(bg="green")

        
        #check if diagonal 2
        if (self.state[0][2] == self.state[1][1] == self.state[2][0] == 1):
            self.done = True
            for j in range(3):
                self.buttons[j][2-j].config(bg="red")

        elif (self.state[0][2] == self.state[1][1] == self.state[2][0] == 2):
            self.done = True
            for j in range(3):
                self.buttons[j][2-j].config(bg="green")

        elif self.if_full() == True:
            self.done = True
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(bg="grey")
    
    def button_click(self, row, column):
         if not self.done:
            if self.state[row][column] == 0 and self.current_player == "X":
                self.buttons[row][column]["text"] = self.current_player
                self.state[row][column] = 1
                self.check()
                self.current_player = "O"

            elif self.state[row][column] == 0 and self.current_player == "O":
                self.buttons[row][column]["text"] = self.current_player
                self.state[row][column] = 2
                self.check()
                self.current_player = "X"
    
    def if_full(self):
         for i in range(3):
            for j in range(3):
                  if self.state[i][j] == 0:
                        return False
                  
         return True
    
    




    