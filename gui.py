import tkinter as tk
from tkinter import font as tkFont
from tkmacosx import Button

from super_tictactoe import SuperTicTacToe
from robot import choose_cell


class TicTacToeApp:
    def __init__(self):
        self.font_size = 30
        self.separator_size = int((1/3) * self.font_size)
        self.empty_button = "    "

        self.game = SuperTicTacToe()

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.minsize((4 * 9 + 1) * self.font_size, (2 * 9 + 3) * self.font_size)
        self.root.rowconfigure((0,2,4), weight=1)  # make self.buttons stretch when
        self.root.columnconfigure((0,2,4), weight=1)  # when window is resized

        self.button_font = tkFont.Font(size=self.font_size)

        self.frames = []
        self.buttons = []

        for a in range(3): # creating the frames in the root window that the grids will be placed in
            row_frames = []
            for b in range(3):
                game_frame = tk.Frame(self.root)
                game_frame.grid(row=2 * a, column=2 * b)
                row_frames.append(game_frame)

                if b < 2: # the horizontal separator 
                    column_separator_frame = tk.Frame(self.root, width=self.separator_size)
                    column_separator_frame.grid(row=2 * a, column=2 * b + 1) 

                    row_frames.append(column_separator_frame)
            
            self.frames.append(row_frames)

            if a < 2: # the vertical seperator 
                row_separator_frame = tk.Frame(self.root, height=self.separator_size)
                row_separator_frame.grid(row=2 * a + 1, columnspan=3)
                self.frames.append(row_separator_frame)


        for a in range(3): #creating the buttons that will call the button_click function
            self.buttons.append([])
            for b in range(3):
                self.buttons[a].append([])

                for c in range(3):
                    self.buttons[a][b].append([])
                    
                    for d in range(3):
                        button = Button(self.frames[2*a][2*b], text = self.empty_button, 
                                        font = self.button_font, height=2*self.font_size, width=4*self.font_size,
                                        command = lambda n= a , m=b ,i=c, j=d: self.button_click(n, m ,i, j))
                        
                        button.grid(row=c , column = d, sticky='EWNS')
                        self.buttons[a][b][c].append(button) 
        
        restart_button = Button(self.root, text="restart game", 
                                command= self.button_reset)
        restart_button.grid(row=7, column=2)

        padding_frame = tk.Frame(self.root, height=self.separator_size)
        padding_frame.grid(row=8, columnspan=3)

    def run(self): 
        self.root.mainloop() 
 
    def button_click(self, n, m, i, j):
        game_updated = self.game.update(n, m, i, j) 

        if game_updated:
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        for d in range(3):
                            self.buttons[a][b][c][d].config(state = "normal")

            self.buttons[n][m][i][j]["text"] = "X"  

            chosen_cell = choose_cell(self.game)
            if chosen_cell is not None:
                n1, m1 , i1 , j1 = chosen_cell
                game_updated = self.game.update(n1, m1, i1, j1)
                if game_updated:
                    self.buttons[n1][m1][i1][j1]["text"] = "O"
                
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        for d in range(3):
                            if (a, b, c, d) not in self.game.available_cells:
                                self.buttons[a][b][c][d].config(state = "disabled")
                            
                            if [c, d] in self.game.games[a][b].winner_cells:
                                self.buttons[a][b][c][d].config(bg = "lawn green" 
                                                                if self.game.games[a][b].won == 1 else "red2")
                    
            if chosen_cell is not None and game_updated:
                self.buttons[n1][m1][i1][j1].config(bg = "cyan")

    def button_reset(self): 
        self.game.reset() 
        
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        self.buttons[a][b][c][d].config(state = "normal", text=self.empty_button, bg="white")
    

    
if __name__ == "__main__":
    app = TicTacToeApp()
    app.run() 
        