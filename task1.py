board = [' '] * 9

def display_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def check_win(player):
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))


def check_full():
    return ' ' not in board


def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()
        move = input("Player " + current_player + ", choose a position (1-9): ")

        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = current_player
                if check_win(current_player):
                    display_board()
                    print("Congratulations! Player " + current_player + " wins!")
                    game_over = True
                elif check_full():
                    display_board()
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. That position is already filled.")
        else:
            print("Invalid move. Please enter a number between 1 and 9.")


play_game()
