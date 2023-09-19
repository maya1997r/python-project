import random # importing the random function to choose a random button for the computer's turn 


def computers_move(game): # a function that takes an instance of the super tic tac toe game and the current player's value

    empty_cells = [] # a list to store the available buttons that the computer can pick from
    chosen_cell = None

    
        # assigning the n and m which indicate which game to choose from according to the indexes of the previously chosed button click from the user
    n, m = game.small_board_position
    if not (game.games[n][m].won != 0 or game.games[n][m].if_full()): # if the game that we should be from is not won yet or it isnt full we add the empty buttons there to the empty_cells list
                

        for i in range(3):
            for j in range(3):
                if game.games[n][m].state[i][j] == 0 :
                        empty_cells.append((n , m, i, j))

    else:  # is the game is either full or won then the buttons are of a wider range 
        for row in range(3):
            for column in range(3):
                if (game.games[row][column].won == 0 or not game.games[row][column].if_full()):
                    for i in range(3):
                        for j in range(3):

                            if (game.games[row][column].state[i][j] == 0 ):
                                empty_cells.append((row , column, i, j))

    if empty_cells: # if there are some empty buttons to choose from 
        chosen_cell = random.choice(empty_cells) # then we choose a random button there(with no AI capabilities)

    return chosen_cell #i found the issue here hahahaha


        