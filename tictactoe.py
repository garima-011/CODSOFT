"""
CODSOFT - Artificial Intelligence Internship
Task 2: Tic-Tac-Toe AI with Minimax Algorithm (Terminal Version)
"""

HUMAN = "X"
AI    = "O"

def print_board(board):
    print("\n")
    for row in range(3):
        cells = []
        for col in range(3):
            val = board[row * 3 + col]
            cells.append(f" {val if val else row*3+col+1} ")
        print("|".join(cells))
        if row < 2:
            print("-----------")
    print("\n")

def check_winner(board, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == player for i in line) for line in wins)

def is_full(board):
    return all(cell != "" for cell in board)

def minimax(board, is_maximizing):
    if check_winner(board, AI):   return 1
    if check_winner(board, HUMAN): return -1
    if is_full(board):             return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = AI
                best = max(best, minimax(board, False))
                board[i] = ""
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = HUMAN
                best = min(best, minimax(board, True))
                board[i] = ""
        return best

def best_move(board):
    best_val, move = -float("inf"), -1
    for i in range(9):
        if board[i] == "":
            board[i] = AI
            val = minimax(board, False)
            board[i] = ""
            if val > best_val:
                best_val, move = val, i
    return move

def play():
    print("=" * 35)
    print("   Tic-Tac-Toe AI  |  CodSoft")
    print("=" * 35)
    print("  You are X  |  AI is O")
    print("  Enter a number (1-9) to play")
    print("  Board positions:")
    print("   1 | 2 | 3 ")
    print("  -----------")
    print("   4 | 5 | 6 ")
    print("  -----------")
    print("   7 | 8 | 9 ")
    print("=" * 35)

    board = [""] * 9

    while True:
        print_board(board)

        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == "":
                    break
                else:
                    print("Invalid! Cell already taken or out of range.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        board[move] = HUMAN

        if check_winner(board, HUMAN):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a Draw!")
            break

        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move] = AI
        print(f"AI played at position {ai_move + 1}")

        if check_winner(board, AI):
            print_board(board)
            print("AI wins! Better luck next time.")
            break

        if is_full(board):
            print_board(board)
            print("It's a Draw!")
            break

    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again in ["yes", "y"]:
        play()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play()
