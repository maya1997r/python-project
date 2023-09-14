import tkinter as tk
from tkinter import font as tkFont
from super_tictactoe import SuperTicTacToe
from tictactoe import Tictactoe
font_size = 30
separator_size = int((1/3) * font_size)

frames = []
game = SuperTicTacToe()
empty_button = "    "
buttons = []


def button_click(n, m , i, j):
    
    played_by, game_update = game.update(n, m, i, j)

    if game_update is not None:

        buttons[n][m][i][j]["text"] = "X" if played_by == 1 else "O"

        if type(game_update) == list:
            for i in range(3):
                buttons[n][m][game_update[i][0]][game_update[i][1]].config(bg = "red" if played_by == 1 else "green")

def button_reset():
    for n in range(3):
        for m in range(3):
            for i in range(3):
                for j in range(3):
                    buttons[n][m][i][j]["text"] = empty_button
    
    game.reset()


if __name__ == "__main__":
    


    root = tk.Tk()
    root.title("Tic Tac Toe")

    root.minsize(16 * font_size, 15 * font_size)
    button_font = tkFont.Font(size=font_size)
    
    

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


    restart_button = tk.Button(root, text="restart game", 
                               command= button_reset)
    restart_button.grid(row=7, column=2)
    padding_frame = tk.Frame(root, height=separator_size)
    padding_frame.grid(row=8, columnspan=3)

    
    
    

    for n in range(3):
        buttons.append([])
        for m in range(3):
            buttons[n].append([])

            for i in range(3):
                buttons[n][m].append([])
                
                for j in range(3):
                    button = tk.Button(frames[2*n][2*m], text = empty_button, 
                                        font = button_font, 
                                        command = lambda n = n , m = m ,i=i, j=j: button_click(n, m ,i, j))
                    
                    button.grid(row=i , column = j, sticky='EWNS')
                    buttons[n][m][i].append(button) 
            
            
            



    root.mainloop()