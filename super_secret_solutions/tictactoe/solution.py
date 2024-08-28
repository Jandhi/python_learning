X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'

# The layout of the board is as follows 
# ┌─┬─┬─┐
# |1|2|3|
# ├─┼─┼─┤
# |4|5|6|
# ├─┼─┼─┤
# |7|8|9|
# └─┴─┴─┘

def tic_tac_toe() -> None:
    board : list[str] = [EMPTY] * 9
    turn : str = X
    victory : str = EMPTY

    while victory == EMPTY:
        print_board(board)
        print(f'It is {turn}\'s turn.')
        move = get_move(board)
        place_move(board, move, turn)
        victory = evalulate_victory(board)

        if turn == X:
            turn = O
        else:
            turn = X

    print_board(board)

    if victory == TIE:
        print(f'It\'s a tie!')
        return

    print(f'{victory} won!')
    
# TODO 
# A function that should enter a player's symbol into the correct position on 
# the board
# position will be a number from 1 to 9
# player will be X or O
def place_move(board : list[str], position : int, player : str):
    board[position - 1] = player

# TODO
# A function that should ask a player in which position they would like to 
# place their move
# If the move is invalid (ie not an empty position on the board), it should
# output an error and prompt the player for input again
def get_move(board : list[str]) -> int:
    print('In which position do you want to place your move?')
    move = input()

    if not move.isdigit():
        print('ERROR: not numeric')
        return get_move(board)
    
    number = int(move)

    if number < 1 or number > 9:
        print('ERROR: out of range')
        return get_move(board)
    
    if board[number - 1] != EMPTY:
        print('ERROR: space not empty')
        return get_move(board)
    
    return number

# TODO
# A function that should return 
#   X if the X player won
#   O if the O player one,
#   EMPTY otherwise 
def evalulate_victory(board : list[str]) -> str:
    # columns
    for i in range(3):
        if (board[i] == X or board[i] == O) and board[i] == board[i + 3] and board[i] == board[i + 6]:
            return board[i]
    
    # rows
    for i in range(3):
        if (board[3 * i + 1] == X or board[3 * i + 1] == O) and board[3 * i + 1] == board[3 * i + 2] and board[3 * i + 1] == board[3 * i + 3]:
            return board[3 * i + 1]
        
    return EMPTY


def print_board(board : list[str]) -> None:
    print(f'┌─┬─┬─┐ ┌─┬─┬─┐')
    print(f'|{board[0]}|{board[1]}|{board[2]}| |1|2|3|')
    print(f'├─┼─┼─┤ ├─┼─┼─┤')
    print(f'|{board[3]}|{board[4]}|{board[5]}| |4|5|6|')
    print(f'├─┼─┼─┤ ├─┼─┼─┤')
    print(f'|{board[6]}|{board[7]}|{board[8]}| |7|8|9|')
    print(f'└─┴─┴─┘ └─┴─┴─┘')


# Runs the main function
tic_tac_toe()