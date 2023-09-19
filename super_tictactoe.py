from tictactoe import SmallTictactoe
from robot import computers_move


class SuperTicTacToe:
    def __init__(self):

        self.current_player = 1
        self.small_board_position = None
        self.empty_cells = [] 

        self.games = []
        for i in range(3):
            games_row = []
            for j in range(3):
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


    def update(self, n, m , i, j):


        game_is_won = self.check_winner() # calling the function to check if a player has won the entire game yet
        if not game_is_won: # if no one won the big game yet so we can continue

            if (self.small_board_position == None or self.small_board_position == [n,m]): # if the button the player or computer pressed is valid
                if (self.games[n][m].if_full() or self.games[n][m].won != 0) : # if the game the player pressed is full or invalid then he can make a move on any other available board 
                    self.small_board_position = None 
                    return None

                game_update = self.games[n][m].update(i, j, self.current_player) # calls a function from the small tic tac toe game to update the states of the small board

                if game_update is not None: # if the small board and button are updated correctly
                    self.small_board_position = [i,j] # then the position of the next game is the position of the button clicked in the small game
                    self.current_player = 2 if self.current_player == 1 else 1 
                    self.available_spaces()

                    return game_update
                
                
                
        return None

    def reset(self): # a function to reset the entire game 
        for i in range(3):
            for j in range(3):
                self.games[i][j].reset()
                
        self.current_player = 1
        self.small_board_position = None


    
    def available_spaces(self):

        

        
            # assigning the n and m which indicate which game to choose from according to the indexes of the previously chosed button click from the user
        n, m = self.small_board_position
        if not (self.games[n][m].won != 0 or self.games[n][m].if_full()): # if the game that we should be from is not won yet or it isnt full we add the empty buttons there to the empty_cells list
                    

            for i in range(3):
                for j in range(3):
                    if self.games[n][m].state[i][j] == 0 :
                            self.empty_cells.append((n , m, i, j))

        else:  # is the game is either full or won then the buttons are of a wider range 
            for row in range(3):
                for column in range(3):
                    if (self.games[row][column].won == 0 or not self.games[row][column].if_full()):
                        for i in range(3):
                            for j in range(3):

                                if (self.games[row][column].state[i][j] == 0 ):
                                    self.empty_cells.append((row , column, i, j))

        

                