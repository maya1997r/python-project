from tictactoe import SmallTictactoe


class SuperTicTacToe:
    def __init__(self):

        self.current_player = 1
        self.small_board_position = None
        self.available_cells = [] 

        self.games = []
        for _ in range(3):
            games_row = []
            for _ in range(3):
                games_row.append(SmallTictactoe())
            self.games.append(games_row)


    def check_winner(self):
        
        for i in range(3):
            # check horizontal winning of the big tic tac toe game
            if (all([j.won == 1 for j in self.games[i]]) or 
                all([j.won == 2 for j in self.games[i]])):
                return True

            # check vertical 
            if (self.games[0][i].won == self.games[1][i].won == self.games[2][i].won == 1 or 
                self.games[0][i].won == self.games[1][i].won == self.games[2][i].won == 2):
                return True

        # Check if diagonal 1
            if (self.games[0][0].won == self.games[1][1].won == self.games[2][2].won == 1 or
                self.games[0][0].won == self.games[1][1].won == self.games[2][2].won == 2):
                return True
            
        # Check if diagonal 2
        if (self.games[0][2].won == self.games[1][1].won == self.games[2][0].won == 1 or
            self.games[0][2].won == self.games[1][1].won == self.games[2][0].won == 2):
            return True

        return False #returns false if no one won the game yet

    def is_full(self):
        for a in range(3):
            for b in range(3):
                if self.games[a][b].won == 0 and not self.games[a][b].is_full():
                    return False
        return True


    def update(self, n, m , i, j):

        if not self.check_winner() and not self.is_full(): # if no one won the big game yet so we can continue

            game_update = self.games[n][m].update(i, j, self.current_player) # calls a function from the small tic tac toe game to update the states of the small board

            self.small_board_position = [i,j] # then the position of the next game is the position of the button clicked in the small game
            self.current_player = 2 if self.current_player == 1 else 1 
            self.available_spaces()

            return game_update


        return None

    def reset(self): # a function to reset the entire game 
        for a in range(3):
            for b in range(3):
                self.games[a][b].reset()
                
        self.current_player = 1
        self.small_board_position = None


    
    def available_spaces(self):

        self.available_cells = []
        # assigning the n and m which indicate which game to choose from according to the indexes of the previously chosed button click from the user
        a, b = self.small_board_position
        if not (self.games[a][b].won != 0 or self.games[a][b].is_full()): # if the game that we should be from is not won yet or it isnt full we add the empty buttons there to the available_cells list
            for c in range(3):
                for d in range(3):
                    if self.games[a][b].state[c][d] == 0 :
                            self.available_cells.append((a , b, c, d))

        else:  # is the game is either full or won then the buttons are of a wider range 
            for a in range(3):
                for b in range(3):
                    if (self.games[a][b].won == 0 or not self.games[a][b].is_full()):
                        for c in range(3):
                            for d in range(3):

                                if (self.games[a][b].state[c][d] == 0 ):
                                    self.available_cells.append((a , b, c, d))

        

                