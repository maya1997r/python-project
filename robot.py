import random # importing the random function to choose a random button for the computer's turn 


def choose_cell(game): # a function that takes an instance of the super tic tac toe game and the current player's value

    chosen_cell = None
    if game.available_cells and not game.check_winner(): # if there are some empty buttons to choose from 
        chosen_cell = random.choice(game.available_cells) # then we choose a random button there(with no AI capabilities)

    return chosen_cell #i found the issue here hahahaha
        