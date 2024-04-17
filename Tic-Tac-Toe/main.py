def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter an integer.")


def check_winner(board):
    lines = [
                board[i] for i in range(3)  # Rows
            ] + [
                [board[i][j] for i in range(3)] for j in range(3)  # Columns
            ] + [
                [board[i][i] for i in range(3)],  # Main diagonal
                [board[i][2 - i] for i in range(3)]  # Anti-diagonal
            ]

    for line in lines:
        if line[0] != 0 and line.count(line[0]) == 3:
            return line[0]

    if all(board[row][col] != 0 for row in range(3) for col in range(3)):
        return -1  # Draw

    return 0  # Game continues


def minimax(board, depth, is_maximizing, player):
    opponent = 3 - player
    winner = check_winner(board)
    if winner != 0:
        return None, (1 if winner == player else -1 if winner == opponent else 0)

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    _, score = minimax(board, depth + 1, False, player)
                    board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move, best_score
    else:
        worst_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = opponent
                    _, score = minimax(board, depth + 1, True, player)
                    board[i][j] = 0
                    if score < worst_score:
                        worst_score = score
                        worst_move = (i, j)
        return worst_move, worst_score


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
        return 3 > row >= 0 == self.board[row][col] and 0 <= col < 3

    def ai_move(self):
        move, _ = minimax(self.board, 0, True, 2)
        if move:
            self.execute_move(*move)


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        print("Current Board:")
        game.display_board()
        if game.current_player == 1:
            row = read_int("Enter row (0-2): ")
            col = read_int("Enter column (0-2): ")
            if not game.execute_move(row, col):
                print("Invalid move, try again.")
                continue
        else:
            print("AI is making a move...")
            game.ai_move()

        winner = check_winner(game.board)
        if winner != 0:
            game.display_board()
            if winner == -1:
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
