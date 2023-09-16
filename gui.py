import tkinter as tk
from tkinter import font as tkFont
from super_tictactoe import SuperTicTacToe


class TicTacToeApp:
    def __init__(self):
        self.font_size = 30
        self.separator_size = int((1/3) * self.font_size)
        self.frames = []
        self.game = SuperTicTacToe()
        self.empty_button = "    "
        self.buttons = []

    def button_click(self, n, m, i, j):
        played_by, game_update = self.game.update(n, m, i, j)

        if game_update is not None:

            self.buttons[n][m][i][j]["text"] = "X" if played_by == 1 else "O"

            if type(game_update) == list:
                for i in range(3):
                    self.buttons[n][m][game_update[i][0]][game_update[i][1]].config(bg = "red" if played_by == 1 else "green")

    def button_reset(self):
        for n in range(3):
            for m in range(3):
                for i in range(3):
                    for j in range(3):
                        self.buttons[n][m][i][j]["text"] = self.empty_button
    
        self.game.reset()

    def run(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.minsize(16 * self.font_size, 15 * self.font_size)
        self.button_font = tkFont.Font(size=self.font_size)
        self.root.rowconfigure((0,2,4), weight=1)  # make self.buttons stretch when
        self.root.columnconfigure((0,2,4), weight=1)  # when window is resized

        for i in range(3):
            row_frames = []
            for j in range(3):
                game_frame = tk.Frame(self.root)
                game_frame.grid(row=2 * i, column=2 * j)
                row_frames.append(game_frame)


                if j < 2:
                    column_separator_frame = tk.Frame(self.root, width=self.separator_size)
                    column_separator_frame.grid(row=2 * i, column=2 * j + 1) 

                    row_frames.append(column_separator_frame)
            
            self.frames.append(row_frames)

            if i < 2:
                row_separator_frame = tk.Frame(self.root, height=self.separator_size)
                row_separator_frame.grid(row=2 * i + 1, columnspan=3)
                self.frames.append(row_separator_frame)


        restart_button = tk.Button(self.root, text="restart game", 
                                command= self.button_reset)
        restart_button.grid(row=7, column=2)
        padding_frame = tk.Frame(self.root, height=self.separator_size)
        padding_frame.grid(row=8, columnspan=3)


        for n in range(3):
            self.buttons.append([])
            for m in range(3):
                self.buttons[n].append([])

                for i in range(3):
                    self.buttons[n][m].append([])
                    
                    for j in range(3):
                        button = tk.Button(self.frames[2*n][2*m], text = self.empty_button, 
                                            font = self.button_font, 
                                            command = lambda n = n , m = m ,i=i, j=j: self.button_click(n, m ,i, j))
                        
                        button.grid(row=i , column = j, sticky='EWNS')
                        self.buttons[n][m][i].append(button) 
            

        self.root.mainloop()

if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()

        