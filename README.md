# Python Tic-Tac-Toe with Minimax Algorithm

This Python script implements a simple Tic-Tac-Toe game where a human player can play against an AI that uses the minimax algorithm. The game is played on a 3x3 board.

## Features

+ **Human vs AI Gameplay**: Play against a computer AI that evaluates moves using the minimax algorithm.
+ **Command Line Interface**: Simple text-based interface to play the game in the command line.
+ **Input Validation**: Ensures that only valid integers are accepted as input.

## Requirements

This script requires *Python 3.x.* No additional libraries are necessary.

## Code Structure

+ *read_int(prompt)*: Function to read and validate integer inputs.
+ *check_winner(board)*: Function to check the current state of the board for a winner or a draw.
+ *minimax(board, depth, is_maximizing, player)*: The minimax function to calculate the best move for the AI.
+ *TicTacToe Class*:
    + Methods to manage game state, validate moves, make moves, and display the board.
 
## Game Flow

1. The game is initiated and the board is displayed.
2. Player 1 (human) is prompted to enter a move.
3. Player 2 (AI) calculates and makes the next move.
4. Steps 2 and 3 repeat until the game ends with a win or a draw, at which point the final board state is displayed along with the result.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests if you have suggestions or improvements. This is a simple educational project and contributions are welcome!
