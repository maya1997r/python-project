from super_tictactoe import SuperTicTacToe
from robot import choose_cell

def controller():
    game = SuperTicTacToe()
    player1_wins = 0
    player2_wins = 0
    games_played = 0
    tied_games = 0

    


    while not game.check_winner() and not game.is_full():
        
        chosen_cell = choose_cell(game)
        if chosen_cell:
            n1, m1, i1, j1 = chosen_cell
            game.update(n1, m1, i1, j1)

        if game.check_winner():
            player1_wins += 1
            games_played += 1
            break
        elif game.is_full():
            games_played += 1
            tied_games +=1
            break

        for n in range(3):
            for m in range(3):
                if game.games[n][m].won == 0 and not game.games[n][m].is_full():
                    for i in range(3):
                        for j in range(3):
                            if game.games[n][m].state[i][j] == 0:
                                game.update(n, m, i, j)
                                break
                    break

        if game.check_winner():
            player2_wins += 1
            games_played += 1
            break
        elif game.is_full():
            games_played += 1
            tied_games +=1
            break

    

    print("Player 1 wins:", player1_wins)
    print("Player 2 wins:", player2_wins)
    print(f"tied games: ", tied_games)
    print("Games played:", games_played)
    

if __name__ == "__main__":
    controller()
