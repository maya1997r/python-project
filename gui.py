import tkinter as tk
from tkinter import font as tkFont
from super_tictactoe import SuperTicTacToe
from robot import computers_move


class TicTacToeApp:
    def __init__(self):
        self.font_size = 30
        self.separator_size = int((1/3) * self.font_size)
        self.frames = []
        self.game = SuperTicTacToe()
        self.empty_button = "    "
        self.buttons = []

    def run(self): # method to start the whole game on the user's window
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.minsize(16 * self.font_size, 15 * self.font_size)
        self.button_font = tkFont.Font(size=self.font_size)
        self.root.rowconfigure((0,2,4), weight=1)  # make self.buttons stretch when
        self.root.columnconfigure((0,2,4), weight=1)  # when window is resized

        for i in range(3): # creating the frames in the root window that the grids will be placed in
            row_frames = []
            for j in range(3):
                game_frame = tk.Frame(self.root)
                game_frame.grid(row=2 * i, column=2 * j)
                row_frames.append(game_frame)


                if j < 2: # the horizontal separator 
                    column_separator_frame = tk.Frame(self.root, width=self.separator_size)
                    column_separator_frame.grid(row=2 * i, column=2 * j + 1) 

                    row_frames.append(column_separator_frame)
            
            self.frames.append(row_frames)

            if i < 2: # the vertical seperator 
                row_separator_frame = tk.Frame(self.root, height=self.separator_size)
                row_separator_frame.grid(row=2 * i + 1, columnspan=3)
                self.frames.append(row_separator_frame)


        restart_button = tk.Button(self.root, text="restart game", 
                                command= self.button_reset) # creating the restart button that will call the reset method when clicked
        restart_button.grid(row=7, column=2)
        padding_frame = tk.Frame(self.root, height=self.separator_size)
        padding_frame.grid(row=8, columnspan=3)


        for n in range(3): #creating the buttons that will call the button_click function
            self.buttons.append([])
            for m in range(3):
                self.buttons[n].append([])

                for i in range(3):
                    self.buttons[n][m].append([])
                    
                    for j in range(3):
                        button = tk.Button(self.frames[2*n][2*m], text = self.empty_button, 
                                            font = self.button_font, 
                                            command = lambda n = n , m = m ,i=i, j=j: self.button_click(n, m ,i, j))
                        
                        button.grid(row=i , column = j, sticky='EWNS') #making the buttons visible on the window
                        self.buttons[n][m][i].append(button) 
            

        self.root.mainloop() # method that loops waiting for events until the user exits
 

    def button_click(self, n, m, i, j): # specifies what is shown on the screen when a button is clicked or a computer move is made
        game_update = self.game.update(n, m, i, j) # calls a function from the supertictactoe to update the state of the game if certain conditions are met 

        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        self.buttons[a][b][c][d]["state"] = "normal"
        if game_update is not None: # meaning if the button clicked or the computer move is valid it the process will continue

            self.buttons[n][m][i][j]["text"] = "X"  # it displays the valid clicked buttons value (either x or o)

            if type(game_update) == list: #checks if there is a winner in the small board, a list indicates that it returned the winners_state list from the small tic tac toe class
                for i in range(3):
                    self.buttons[n][m][game_update[i][0]][game_update[i][1]].config(bg = "red" ) #if the condition above is met then it changes the colors of the winners small board

            if not self.game.check_winner():
                computer_move = computers_move(self.game)
                if computer_move is not None:
                    n1, m1 , i1 , j1 = computer_move
                    game_update = self.game.update(n1, m1, i1, j1)
                    self.buttons[n1][m1][i1][j1]["text"] = "O"  
                    if type(game_update) == list: #checks if there is a winner in the small board, a list indicates that it returned the winners_state list from the small tic tac toe class
                        for i in range(3):
                            self.buttons[n][m][game_update[i][0]][game_update[i][1]].config(bg = "green")
                    for a in range(3):
                        for b in range(3):
                            for c in range(3):
                                for d in range(3):
                                    if (a, b, c, d) not in self.game.empty_cells:
                                        self.buttons[a][b][c][d]["state"] = "disabled"

                    

    def button_reset(self): # a function to reset all the buttons text values to empty on the screen
        for n in range(3):
            for m in range(3):
                for i in range(3):
                    for j in range(3):
                        self.buttons[n][m][i][j]["text"] = self.empty_button
    
        self.game.reset() # to reset all the buttons states in the supertictactoe

    
if __name__ == "__main__":
    app = TicTacToeApp()
    app.run() # calling the run method from the class and starting the whole game
        