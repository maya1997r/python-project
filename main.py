import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from tictactoe import Tictactoe
font_size = 30
separator_size = int((1/3) * font_size)

frames = []
games = []
empty_button = "    "
buttons = []
current_player = 1


def button_click(n, m , i, j):
    
    global current_player
    game_update = games[n][m].update(i,j,current_player)

    if game_update is not None:
        if current_player == 1:
            buttons[n][m][i][j]["text"] = "X"
            current_player = 2

        elif current_player == 2:
            buttons[n][m][i][j]["text"] = "O"
            current_player = 1





if __name__ == "__main__":
    print("hinndkjnksjndjksnk")


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

    
    for i in range(3):
        row_games = []
        for j in range(3):
            game = Tictactoe(frames[2 * i][2 * j])
            row_games.append(game)
        games.append(row_games)

    restart_button = tk.Button(root, text="restart game", 
                               command=lambda: [[game.reset() for game in row] for row in games])
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