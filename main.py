import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
from python_project import Tictactoe

font_size = 30
separator_size = int((1/3) * font_size)


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