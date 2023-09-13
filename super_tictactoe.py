from tictactoe import Tictactoe
import tkinter as tk
from tkinter import font as tkFont

class SuperTicTacToe:
    def __init__(self):

        self.current_player = 1
        self.small_board_position = None

        self.games = []
        for i in range(3):
            games_row = []
            for j in range(3):
                games_row.append(Tictactoe())
            self.games.append(games_row)


    def update(self, n, m , i, j):

        if (self.small_board_position == None or self.small_board_position == [n,m]):
            game_update = self.games[n][m].update(i, j, self.current_player)

            print(game_update)

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