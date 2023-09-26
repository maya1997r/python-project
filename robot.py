import random 


def choose_cell(game): 
    chosen_cell = None
    if game.available_cells and not game.check_winner(): 
        chosen_cell = random.choice(game.available_cells) 

    return chosen_cell 
        