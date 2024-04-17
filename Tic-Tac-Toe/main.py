def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")


class TicTacToe:
    def __init__(self):
        self.board = [[0] * 3 for _ in range(3)]
        self.current_player = 1  # Start with player 1

    def execute_move(self, row, col):
        if self.valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 3 - self.current_player  # Toggle between 1 and 2
            return True
        return False

    def display_board(self):
        symbols = {0: ".", 1: "X", 2: "O"}
        for row in self.board:
            print(' '.join(symbols[cell] for cell in row))

    def valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == 0

    def check_winner(self):
        lines = [
                    self.board[i] for i in range(3)  # Rows
                ] + [
                    [self.board[i][j] for i in range(3)] for j in range(3)  # Columns
                ] + [
                    [self.board[i][i] for i in range(3)],  # Main diagonal
                    [self.board[i][2 - i] for i in range(3)]  # Anti-diagonal
                ]

        for line in lines:
            if line[0] != 0 and line.count(line[0]) == 3:
                return line[0]

        if all(self.board[row][col] != 0 for row in range(3) for col in range(3)):
            return -1  # Draw

        return 0  # Game continues


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        print("Current Board:")
        game.display_board()
        row = read_int("Enter row (0-2): ")
        col = read_int("Enter column (0-2): ")

        if not game.execute_move(row, col):
            print("Invalid move, try again.")
            continue

        winner = game.check_winner()
        if winner != 0:
            game.display_board()
            if winner == -1:
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
