import tkinter as tk
from tkinter import messagebox




class Tictactoe:
    def __init__(self, root):
          self.root = root
          self.root.title("Tic Tac Toe")
          self.a = "X"

          

          self.create()
          
          


    def create(self):
        
        frame = tk.Frame(root)
        frame.pack()
        self.buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(frame, text = " " , height=5 , width= 20, command = lambda i=i, j=j: self.button_click(i, j))
                self.buttons[i][j].grid(row=i , column = j)


    def reset(self):
         for i in range(3):
            for j in range(3):
                 self.buttons[i][j]["text"] = " "
                 self.buttons[i][j].config(bg="white")
    
    def check(self, row,column):
         for i in range(3):
            # check if vertical
                if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != " ":
                    
                    self.buttons[i][0].config(bg="red")
                    self.buttons[i][1].config(bg="red")
                    self.buttons[i][2].config(bg="red")
                    messagebox.showinfo(f" {self.a} you won")
                    self.reset()

                elif self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != " ":
                    
                    self.buttons[0][i].config(bg="red")
                    self.buttons[1][i].config(bg="red")
                    self.buttons[2][i].config(bg="red")
                    messagebox.showinfo(f" {self.a} you won")
                    self.reset()

                elif self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != " ":
                    self.buttons[0][0].config(bg="red")
                    self.buttons[1][1].config(bg="red")
                    self.buttons[2][2].config(bg="red")
                    messagebox.showinfo(f" {self.a} you won")
                    
                    self.reset()
                elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != " ":
                    
                    self.buttons[0][2].config(bg="red")
                    self.buttons[1][1].config(bg="red")
                    self.buttons[2][0].config(bg="red")
                    messagebox.showinfo(f" {self.a} you won")
                    self.reset()

                elif self.if_full() == True:
                     self.reset()
    
    def button_click(self, row, column):
         if self.buttons[row][column]["text"] == " " and self.a == "X":
            self.buttons[row][column]["text"] = self.a
            self.check(row,column)
            self.a = "Y"

         elif self.buttons[row][column]["text"] == " " and self.a == "Y":
              self.buttons[row][column]["text"] = self.a
              self.check(row,column)
              self.a = "X"
    
    def if_full(self):
         for i in range(3):
            for j in range(3):
                  if self.buttons[i][j]["text"] == " ":
                        return False
                  
         return True
    
    

if __name__ == "__main__":
    root = tk.Tk()
    game = Tictactoe(root)

    root.mainloop()