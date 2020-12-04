import copy
import Board
import random
import Move


class GamePlayer:

    def __init__(self, max_depth=None, player_colour=None):
        self.max_depth = 2
        self.player_colour = 1
        if max_depth != None and player_colour != None:
            self.max_depth = max_depth
            self.player_colour = player_colour

    def mini_max(self, board_o):
        if self.player_colour == board_o.B:
            board_n = Board.Board(board_o)
            return self.g_max(board_n, 0)
        else:
            board_n = Board.Board(board_o)
            return self.g_min(board_n, 0)

    def g_max(self, board, depth):
        if board.terminal_state() or depth == self.max_depth:
            last_move = Move.Move(board.get_last_move().get_row(), board.get_last_move().get_col())
            return last_move
        children = board.get_children(1)
        max_move = Move.Move(-1000)
        max_score = board.victor()
        # temp_board = Board.Board()
        for child in children:
            move = self.g_min(child, depth+1)
            temp_board = copy.deepcopy(child)
            temp_board.make_move(move.get_row(), move.get_col(), move.get_val())
            if temp_board.victor() >= max_score:
                if temp_board.victor() == max_score:
                    if random.randint(0, 1) == 0:
                        max_move.set_row(child.get_last_move().get_row())
                        max_move.set_col(child.get_last_move().get_col())
                        max_move.set_val(move.get_val())
                        max_score = board.victor()
                else:
                    max_move.set_row(child.get_last_move().get_row())
                    max_move.set_col(child.get_last_move().get_col())
                    max_move.set_val(move.get_val())
                    max_score = board.victor()
        return max_move

    def g_min(self, board, depth):
        if board.terminal_state() or depth == self.max_depth:
            last_move = Move.Move(board.get_last_move().get_row(), board.get_last_move().get_col())
            return last_move
        children = board.get_children(-1)
        min_move = Move.Move(1000)
        min_score = board.victor()
        # temp_board = Board.Board()
        for child in children:
            move = self.g_max(child, depth+1)
            temp_board = copy.deepcopy(child)
            temp_board.make_move(move.get_row(), move.get_col(), move.get_val())
            if temp_board.victor() <= min_score:
                if temp_board.victor() == min_score:
                    if random.randint(0, 1) == 0:
                        min_move.set_row(child.get_last_move().get_row())
                        min_move.set_col(child.get_last_move().get_col())
                        min_move.set_val(move.get_val())
                        min_score = child.victor()
                else:
                    min_move.set_row(child.get_last_move().get_row())
                    min_move.set_col(child.get_last_move().get_col())
                    min_move.set_val(move.get_val())
                    min_score = child.victor()
        return min_move

