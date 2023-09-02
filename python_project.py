import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("tik tak toe")


#make the grid inside a frame

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()



buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

def button_click(row, column):
    buttons[row][column]["text"] = "X"


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(frame, text = "0" , command = lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i , column = j)









root.mainloop()