import GamePlayer
import Board
import Move

#defining minimax depth, anything above a 7 is not advisable :)
depth = input("Choose the depth for the minimax algorithm: ")
B_player = GamePlayer.GamePlayer(int(depth), 1)
W_player = GamePlayer.GamePlayer(int(depth), -1)
board = Board.Board()

# player is always black
ans = input("Black is the color that plays first, do you want to get black? (y/any other key): ")
board.set_last_colour(-1)
board.print()

while not board.terminal_state():
    print()
    case = board.get_last_colour()
    # black's turn to move
    if case == -1:
        print("Black Colour's Turn")
        if ans == 'y':
            # row = -1
            # col = -1
            row = input("Row in which to place piece: ")
            col = input("Column in which to place piece: ")
            while board.valid_move(int(row), int(col)) == 0:
                print("Error: Invalid move, try again...")
                row = input("Row in which to place piece: ")
                col = input("Column in which to place piece: ")
            board.make_move(int(row), int(col), 1)

        else:
            while True:
                B_move: Move = B_player.mini_max(board)
                if board.valid_move(B_move.get_row(), B_move.get_col()) != 0:
                    board.make_move(B_move.get_row(), B_move.get_col(), 1)
                    print("Black moved to: ", B_move.get_row(), "/", B_move.get_col())
                    break
        board.set_last_colour(1)

    # white's turn to move
    elif case == 1:
        print("White Colour's Turn")
        if ans == 'y':
            while True:
                W_move: Move = W_player.mini_max(board)
                if board.valid_move(W_move.get_row(), W_move.get_col()) != 0:
                    board.make_move(W_move.get_row(), W_move.get_col(), -1)
                    print("White moved to: ", W_move.get_row(), "/" , W_move.get_col())
                    break
        else:
            # row = -1
            # col = -1

            row = input("Row in which to place piece: ")
            col = input("Column in which to place piece: ")
            while board.valid_move(int(row), int(col)) == 0:
                print("Error: Invalid move, try again...")
                row = input("Row in which to place piece: ")
                col = input("Column in which to place piece: ")
            board.make_move(int(row), int(col), -1)
        board.set_last_colour(-1)
    board.print()

if board.victor() > 0:
    print("Black Wins!")
elif board.victor() < 0:
    print("White wins!")
else:
    print("Draw!")




