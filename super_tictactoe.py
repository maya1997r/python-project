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
            if (all([self.games[i][j].won == 1 for j in range(3)]) or 
                all([self.games[i][j].won == 2 for j in range(3)])):
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

        if not self.check_winner() and not self.is_full(): 

            game_updated = self.games[n][m].update(i, j, self.current_player)

            if game_updated:
                self.small_board_position = [i,j] 
                self.current_player = 2 if self.current_player == 1 else 1 
                self.update_available_cells()
                return True
            else:
                print(f"Small Game {n}, {m}")
            
        return False
    
    def update_available_cells(self):

        self.available_cells = []
        
        n, m = self.small_board_position
        if self.games[n][m].won == 0 and not self.games[n][m].is_full():
            for i in range(3):
                for j in range(3):
                    if self.games[n][m].state[i][j] == 0:
                        self.available_cells.append((n , m, i, j))

        else:  
            for a in range(3):
                for b in range(3):
                    if self.games[a][b].won == 0 and not self.games[a][b].is_full():
                        for c in range(3):
                            for d in range(3):
                                if self.games[a][b].state[c][d] == 0:
                                    self.available_cells.append((a , b, c, d))

    def reset(self):
        for a in range(3):
            for b in range(3):
                self.games[a][b].reset()
                
        self.current_player = 1
        self.small_board_position = None

                