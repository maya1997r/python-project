import random 


def computers_move(game, current_player):

    empty_cells = []

    if current_player == 2:

        n, m = game.small_board_position

        if (n , m) != None:

            for i in range(3):
                for j in range(3):
                    if game.games[n][m].state[i][j] == 0:
                        empty_cells.append((n , m, i, j))


            if empty_cells:
                chosen_cell = random.choice(empty_cells)

            return (n, m, chosen_cell[2], chosen_cell[3])
        

    return None


        