import tkinter as tk
from tkinter import messagebox
# Create the main window
root = tk.Tk()
root.title("tik tak toe")


#make the grid inside a frame

frame = tk.Frame(root)
frame.pack(padx=10, pady= 30)


buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

a = "X"

def reset():
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(frame, text = " " , height=10 , width= 20, command = lambda i=i, j=j: button_click(i, j))
            buttons[i][j].grid(row=i , column = j)


def if_full():
      for i in range(3):
            for j in range(3):
                  if buttons[i][j]["text"] == " ":
                        return False
                  
      return True
                  
            

     
      





def check(row, column):
        
        

        
            for i in range(3):
            # check if vertical
                if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != " ":
                    messagebox.showinfo(f" {a} you won")
                    reset()

                elif buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != " ":
                    messagebox.showinfo(f" {a} you won")
                    reset()

                elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != " ":
                    messagebox.showinfo(f" {a} you won")
                    reset()
                elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != " ":
                    messagebox.showinfo(f" {a} you won")
                    reset()

                elif if_full() == True:
                     reset()

                
def button_click(row, column):   
        global a
        if buttons[row][column]["text"] == " " and a == "X":
            buttons[row][column]["text"] = a
            check(row,column)
            a = "Y"

        elif buttons[row][column]["text"] == " " and a == "Y":
            buttons[row][column]["text"] = a
            check(row,column)
            a = "X"

           


reset()
root.mainloop()