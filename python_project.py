import tkinter as tk
from tkinter import messagebox

frame_width = 90
frame_height = 45

class Tictactoe:
    def __init__(self, frame):
        
        
        #self.root.geometry(f"{window_width}x{window_height}")
        self.current_player = "X"

        
        self.state = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
        
        self.buttons = []


        for i in range(3):
            self.buttons.append([])
            for j in range(3):
                button = tk.Button(frame, text = " " , height= int((1/9) * frame_height), width= int((1/9) * frame_width), command = lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i , column = j)
                self.buttons[i].append(button)

          

          


    def reset(self):
         for i in range(3):
            for j in range(3):
                 self.buttons[i][j]["text"] = " "
                 self.buttons[i][j].config(bg="white")
                 self.state[i][j] = 0
    
    def check(self, row,column):
         for i in range(3):
            # check if vertical
                if (self.state[i][0] == self.state[i][1] == self.state[i][2] == 1) or (self.state[i][0] == self.state[i][1] == self.state[i][2] == 2):
                    
                    self.buttons[i][0].config(bg="red")
                    self.buttons[i][1].config(bg="red")
                    self.buttons[i][2].config(bg="red")
                    messagebox.showinfo(f" {self.current_player} you won")
                    self.reset()

                elif (self.state[0][i] == self.state[1][i] == self.state[2][i] == 1) or (self.state[0][i] == self.state[1][i] == self.state[2][i] == 2):
                    
                    self.buttons[0][i].config(bg="red")
                    self.buttons[1][i].config(bg="red")
                    self.buttons[2][i].config(bg="red")
                    messagebox.showinfo(f" {self.current_player} you won")
                    self.reset()

                elif (self.state[0][0] == self.state[1][1] == self.state[2][2] == 1) or (self.state[0][0] == self.state[1][1] == self.state[2][2] == 2):
                    self.buttons[0][0].config(bg="red")
                    self.buttons[1][1].config(bg="red")
                    self.buttons[2][2].config(bg="red")
                    messagebox.showinfo(f" {self.current_player} you won")
                    
                    self.reset()
                elif (self.state[0][2] == self.state[1][1] == self.state[2][0] == 1) or (self.state[0][2] == self.state[1][1] == self.state[2][0] == 2):
                    
                    self.buttons[0][2].config(bg="red")
                    self.buttons[1][1].config(bg="red")
                    self.buttons[2][0].config(bg="red")
                    messagebox.showinfo(f" {self.current_player} you won")
                    self.reset()

                elif self.if_full() == True:
                     self.reset()
    
    def button_click(self, row, column):
         if self.state[row][column] == 0 and self.current_player == "X":
            self.buttons[row][column]["text"] = self.current_player
            self.state[row][column] = 1
            self.check(row,column)
            self.current_player = "Y"

         elif self.state[row][column] == 0 and self.current_player == "Y":
              self.buttons[row][column]["text"] = self.current_player
              self.state[row][column] = 2
              self.check(row,column)
              self.current_player = "X"
    
    def if_full(self):
         #all(self.state, lambda row: all(row, lambda x: x!= 0))
         for i in range(3):
            for j in range(3):
                  if self.state[i][j] == 0:
                        return False
                  
         return True
    
    

if __name__ == "__main__":


    root = tk.Tk()
    root.title("Tic Tac Toe")

    frames = []

    for i in range(3):
        row_frames = []
        for j in range(3):
            frame = tk.Frame(root)
            frame.grid(row=i, column=j)
            row_frames.append(frame)
        frames.append(row_frames)

    games = []
    for i in range(3):
        row_games = []
        for j in range(3):
            game = Tictactoe(frames[i][j])
            row_games.append(game)
        games.append(row_games)

    restart_button = tk.Button(root, text="restart game", command=lambda: [game.reset() for row in games])
    restart_button.grid()

    root.mainloop()