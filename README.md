# Super Tictactoe
This is an implementation of super tictactoe in python.

The super tictactoe game consists of 9 tictactoe games aranged in 3 rows and 3 columns as the traditional game.

The game goes as follows:

The first player (X) plays in any of 9x9 cells.
The second player (O) then must play anywhere within the subgame matching the location within the subgame where the first player played.
The first player must now play within the subgame matching the location where the second player played.
This continues back and forth.

In case the subgame where the player must play is already won or filled without a winner, the player whose turn it is can choose freely any subgame that is still active.

A player wins when they win 3 games forming a line as in the traditional game.
