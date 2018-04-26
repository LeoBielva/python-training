# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
import random

test_board = ['#', '', '', '', '', '', '', '', '', '']


def display_board(board):
    print(board[7] + '__|__' + board[8] + '__|__' + board[9])
    print(board[4] + '__|__' + board[5] + '__|__' + board[6])
    print(board[1] + '__|__' + board[2] + '__|__' + board[3])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 choose X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[6] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 1:
        print("Player 1 turn...")
    else:
        print("Player 2 turn...")


def space_check(board, position):
    return board[position] == "X" or "O"


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))

    return position


def replay():
    decision = str(input("Do you wish to keep playing? Enter 'Yes' or 'No'\n "))
    return decision == 'Yes'


def main():
    while True:
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn)

        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break


if __name__ == '__main__':
    main()
