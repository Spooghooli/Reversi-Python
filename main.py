import GamePlayer
import Board
import Move


depth = input("Choose the depth for the minimax algorithm: ")
B_player = GamePlayer.GamePlayer(int(depth), 1)
W_player = GamePlayer.GamePlayer(int(depth), -1)
board = Board.Board()

ans = input("Player Gets Black, do you want to play first? (y/any other key): ")
if ans == 'y':
    board.set_last_colour(-1)
else:
    board.set_last_colour(1)

board.print()
while not board.terminal_state():
    print()
    case = board.get_last_colour()
    if case == -1:
        print("Black Colour's Turn")
        row = input("Row in which to place piece: ")
        col = input("Column in which to place piece: ")
        while board.valid_move(int(row), int(col)) == 0:
            print("Error: Invalid move, try again...")
            row = input("Row in which to place piece: ")
            col = input("Column in which to place piece: ")
        board.make_move(int(row), int(col), 1)
        board.set_last_colour(1)
    elif case == 1:
        print("White Colour's Turn")
        while True:
            W_move: Move = W_player.mini_max(board)
            if board.valid_move(W_move.get_row(), W_move.get_col()) != 0:
                board.make_move(W_move.get_row(), W_move.get_col(), -1)
                print("White moved to: ", W_move.get_row(), "/" , W_move.get_col())
                break
        board.set_last_colour(-1)
    board.print()
if board.victor() > 0:
    print("Black Wins!")
elif board.victor() < 0:
    print("White wins!")
else:
    print("Draw!")




