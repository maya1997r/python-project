import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

font_size = 45 
separator_size = int((1/3) * font_size)

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
                                           highlightbackground=None)
                 self.state[i][j] = 0
    
    def check(self):
        for i in range(3):
            # check if horizontal
            if (all([j == 1 for j in self.state[i]])):
                self.done = True
                for j in range(3):
                    self.buttons[i][j].config(highlightbackground="red")

            elif (all([j == 2 for j in self.state[i]])):
                self.done = True
                for j in range(3):
                    self.buttons[i][j].config(highlightbackground="green")

            # check if vertical 
            if (self.state[0][i] == self.state[1][i] == self.state[2][i] == 1):
                self.done = True
                for j in range(3):
                    self.buttons[j][i].config(highlightbackground="red")

            elif (self.state[0][i] == self.state[1][i] == self.state[2][i] == 2):
                self.done = True
                for j in range(3):
                    self.buttons[j][i].config(highlightbackground="green")

        #check if diagonal 1
        if (self.state[0][0] == self.state[1][1] == self.state[2][2] == 1):
            self.done = True
            for j in range(3):
                self.buttons[j][j].config(highlightbackground="red")

        elif (self.state[0][0] == self.state[1][1] == self.state[2][2] == 2):
            self.done = True
            for j in range(3):
                self.buttons[j][j].config(highlightbackground="green")

        
        #check if diagonal 2
        if (self.state[0][2] == self.state[1][1] == self.state[2][0] == 1):
            self.done = True
            for j in range(3):
                self.buttons[j][2-j].config(highlightbackground="red")

        elif (self.state[0][2] == self.state[1][1] == self.state[2][0] == 2):
            self.done = True
            for j in range(3):
                self.buttons[j][2-j].config(highlightbackground="green")

        elif self.if_full() == True:
            self.done = True
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(highlightbackground="grey")
    
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
    
    

if __name__ == "__main__":


    root = tk.Tk()
    root.title("Tic Tac Toe")

    root.minsize(16 * font_size, 15 * font_size)
    button_font = tkFont.Font(size=font_size)
    
    frames = []
    games = []

    root.rowconfigure((0,2,4), weight=1)  # make buttons stretch when
    root.columnconfigure((0,2,4), weight=1)  # when window is resized
    for i in range(3):
        row_frames = []
        for j in range(3):
            game_frame = tk.Frame(root)
            game_frame.grid(row=2 * i, column=2 * j)
            row_frames.append(game_frame)


            if j < 2:
                column_separator_frame = tk.Frame(root, width=separator_size)
                column_separator_frame.grid(row=2 * i, column=2 * j + 1) 

                row_frames.append(column_separator_frame)
        
        frames.append(row_frames)

        if i < 2:
            row_separator_frame = tk.Frame(root, height=separator_size)
            row_separator_frame.grid(row=2 * i + 1, columnspan=3)
            frames.append(row_separator_frame)

    
    for i in range(3):
        row_games = []
        for j in range(3):
            game = Tictactoe(frames[2 * i][2 * j], button_font)
            row_games.append(game)
        games.append(row_games)

    restart_button = tk.Button(root, text="restart game", 
                               command=lambda: [[game.reset() for game in row] for row in games])
    restart_button.grid(row=7, column=2)
    padding_frame = tk.Frame(root, height=separator_size)
    padding_frame.grid(row=8, columnspan=3)

    root.mainloop()