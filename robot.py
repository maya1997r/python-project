import random 


def computers_move(game, current_player):

    empty_cells = []

    if current_player == 2:

        n, m = game.small_board_position

        if n is not None and m is not None:
            if not (game.games[n][m].won != 0 or game.games[n][m].if_full()):
                        

                for i in range(3):
                    for j in range(3):
                       if game.games[n][m].state[i][j] == 0 :
                                empty_cells.append((n , m, i, j))

            else: 
                for row in range(3):
                    for column in range(3):
                        if (game.games[row][column].won == 0 or not game.games[n][m].if_full()):
                            for i in range(3):
                                for j in range(3):

                                    if (game.games[row][column].state[i][j] == 0 ):
                                        empty_cells.append((row , column, i, j))



        




        


            if empty_cells:
                chosen_cell = random.choice(empty_cells)

            return (n, m, chosen_cell[2], chosen_cell[3])
        

    return None


        