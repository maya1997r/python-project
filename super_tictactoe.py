from tictactoe import SmallTictactoe
from robot import computers_move


class SuperTicTacToe:
    def __init__(self):

        self.current_player = 1
        self.small_board_position = None
        self.states = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        self.games = []
        for i in range(3):
            games_row = []
            for j in range(3):
                games_row.append(SmallTictactoe())
            self.games.append(games_row)


    def check_winner(self):
        for n in range(3):
            for m in range(3):
                self.states[n][m] = self.games[n][m].won


        for i in range(3):
            # check horizontal
            if (all([j == 1 for j in self.states[i]]) or 
                all([j == 2 for j in self.states[i]])):
                return True

            # check vertical 
            if (self.states[0][i] == self.states[1][i] == self.states[2][i] == 1 or 
                self.states[0][i] == self.states[1][i] == self.states[2][i] == 2):
                return True

        # Check if diagonal 1
            if (self.states[0][0] == self.states[1][1] == self.states[2][2] == 1 or
            self.states[0][0] == self.states[1][1] == self.states[2][2] == 2):
                return True
            
        # Check if diagonal 2
        if (self.states[0][2] == self.states[1][1] == self.states[2][0] == 1 or
            self.states[0][2] == self.states[1][1] == self.states[2][0] == 2):
            return True
        
        return False


    def update(self, n, m , i, j):


        game_is_won = self.check_winner()

        if self.current_player == 2:

            move = computers_move(self, self.current_player)

            if move is not None:
                n, m, i,j = move


            

        if not game_is_won:

            if (self.small_board_position == None or self.small_board_position == [n,m]):
                if (self.games[n][m].if_full() or self.games[n][m].won != 0) :
                    self.small_board_position = None
                    return

                game_update = self.games[n][m].update(i, j, self.current_player)

                if game_update is not None:
                    self.small_board_position = [i,j]

                    played = self.current_player
                    self.current_player = 2 if self.current_player == 1 else 1

                    return played, game_update
                
                
        return None, None

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.games[i][j].reset()
                
        self.current_player = 1
        self.small_board_position = None


    

            

        