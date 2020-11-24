import Move
import copy


class Board:

    def __init__(self, board=None):
        self.B = 1
        self.W = -1
        self.EMPTY = 0
        self.last_move = Move.Move()
        self.last_colour = -1
        self.game_board = [[0 for x in range(10)] for y in range(10)]
        self.game_board[3][3], self.game_board[3][4] = self.W, self.B
        self.game_board[4][3], self.game_board[4][4] = self.B, self.W
        if board != None:
            self.last_move = board.last_move
            self.last_colour = board.last_colour
            self.game_board = board.game_board.copy()

    def get_last_move(self):
        return self.last_move

    def get_last_colour(self):
        return self.last_colour

    def get_game_board(self):
        return self.game_board

    def set_last_move(self, last_move):
        self.last_move = last_move

    def set_last_colour(self, last_colour):
        self.last_colour = last_colour

    def set_game_board(self, game_board):
        self.game_board = game_board

    def make_move(self, row, col, colour):  # this method is the one that makes the moves
        i: int = row
        j: int = col
        score: int = 0

        while self.valid_move(row, col) != 0:
            if self.game_board[row - 1][col] == self.last_colour:  # up
                i = row
                j = 0
                while self.game_board[i - 1][col] == self.last_colour:
                    i -= 1
                    j += 1
                if self.game_board[i - 1][col] == self.last_colour * -1:
                    for k in range(j):
                        self.game_board[i][col] = colour
                        i += 1

            if self.game_board[row][col - 1] == self.last_colour:  # left
                i = col
                j = 0
                while self.game_board[row][i - 1] == self.last_colour:
                    i -= 1
                    j += 1
                if self.game_board[row][i - 1] == self.last_colour * -1:
                    for k in range(j):
                        self.game_board[row][i] = colour
                        i += 1

            if self.game_board[row + 1][col] == self.last_colour:  # down
                i = row
                j = 0
                while self.game_board[i + 1][col] == self.last_colour:
                    i += 1
                    j += 1
                if self.game_board[i + 1][col] == self.last_colour * -1:
                    for k in range(j):
                        self.game_board[i][col] = colour
                        i -= 1

            if self.game_board[row][col + 1] == self.last_colour:  # right
                i = col
                j = 0
                while self.game_board[row][i + 1] == self.last_colour:
                    i += 1
                    j += 1
                if self.game_board[row][i + 1] == self.last_colour * -1:
                    for k in range(j):
                        self.game_board[row][i] = colour
                        i -= 1

            if self.game_board[row + 1][col + 1] == self.last_colour:  # down & right
                i = row
                k = col
                j = 0
                while self.game_board[i + 1][k + 1] == self.last_colour:
                    i += 1
                    k += 1
                    j += 1
                if self.game_board[i + 1][k + 1] == self.last_colour * -1:
                    for m in range(j):
                        self.game_board[i][k] = colour
                        i -= 1
                        k -= 1

            if self.game_board[row + 1][col - 1] == self.last_colour:  # down & left
                i = row
                k = col
                j = 0
                while self.game_board[i + 1][k - 1] == self.last_colour:
                    i += 1
                    k -= 1
                    j += 1
                if self.game_board[i + 1][k - 1] == self.last_colour * -1:
                    for m in range(j):
                        self.game_board[i][k] = colour
                        i -= 1
                        k += 1

            if self.game_board[row - 1][col + 1] == self.last_colour:  # up & right
                i = row
                k = col
                j = 0
                while self.game_board[i - 1][k + 1] == self.last_colour:
                    i -= 1
                    k += 1
                    j += 1
                if self.game_board[i - 1][k + 1] == self.last_colour * -1:
                    for m in range(j):
                        self.game_board[i][k] = colour
                        i += 1
                        k -= 1

            if self.game_board[row - 1][col - 1] == self.last_colour:  # up & left
                i = row
                k = col
                j = 0
                while self.game_board[i - 1][k - 1] == self.last_colour:
                    i -= 1
                    k -= 1
                    j += 1
                if self.game_board[i - 1][k - 1] == self.last_colour * -1:
                    for m in range(j):
                        self.game_board[i][k] = colour
                        i += 1
                        k += 1

        # after all the other squares are done change the last one and exit
        self.game_board[row][col] = colour
        self.last_move = Move.Move(row, col, colour)
        self.last_colour = colour
        return

    def valid_move(self, row: int, col: int): # this method is the one that checks if the moves are correct
        i: int = row
        j: int = col
        score: int = 0
        try:
            if (row < 0) or (col < 0) or (row > 7) or (col > 7) or self.game_board[row][col] != self.EMPTY:
                return 0
            if self.game_board[row - 1][col] == self.last_colour:  # up
                i = row
                j = col
                score = 0
                while self.game_board[i - 1][j] == self.last_colour:
                    score += 1
                    i -= 1
                if self.game_board[i - 1][j] == self.last_colour * -1:
                    return score
            if self.game_board[row][col - 1] == self.last_colour:  # left
                i = row
                j = col
                score = 0
                while self.game_board[i][j - 1] == self.last_colour:
                    score += 1
                    j -= 1
                if self.game_board[i][j - 1] == self.last_colour * -1:
                    return score
            if self.game_board[row + 1][col] == self.last_colour:  # down
                i = row
                j = col
                score = 0
                while self.game_board[i + 1][j] == self.last_colour:
                    score += 1
                    i += 1
                if self.game_board[i + 1][j] == self.last_colour * -1:
                    return score
            if self.game_board[row][col + 1] == self.last_colour:  # right
                i = row
                j = col
                score = 0
                while self.game_board[i][j + 1] == self.last_colour:
                    score += 1
                    j += 1
                if self.game_board[i][j + 1] == self.last_colour * -1:
                    return score
            if self.game_board[row + 1][col + 1] == self.last_colour:  # down & right
                i = row
                j = col
                score = 0
                while self.game_board[i + 1][j + 1] == self.last_colour:
                    score += 1
                    i += 1
                    j += 1
                if self.game_board[i + 1][j + 1] == self.last_colour * -1:
                    return score
            if self.game_board[row + 1][col - 1] == self.last_colour:  # down & left
                i = row
                j = col
                score = 0
                while self.game_board[i + 1][j - 1] == self.last_colour:
                    score += 1
                    i += 1
                    j -= 1
                if self.game_board[i + 1][j - 1] == self.last_colour * -1:
                    return score
            if self.game_board[row - 1][col + 1] == self.last_colour:  # up & right
                i = row
                j = col
                score = 0
                while self.game_board[i - 1][j + 1] == self.last_colour:
                    score += 1
                    i -= 1
                    j += 1
                if self.game_board[i - 1][j + 1] == self.last_colour * -1:
                    return score
            if self.game_board[row - 1][col - 1] == self.last_colour:  # up & left
                i = row
                j = col
                score = 0
                while self.game_board[i - 1][j - 1] == self.last_colour:
                    score += 1
                    i -= 1
                    j -= 1
                if self.game_board[i - 1][j - 1] == self.last_colour * -1:
                    return score
            return 0
        except IndexError:
            return 0

    def get_children(self, colour):
        children = []
        for i in range(8):
            for j in range(8):
                if self.valid_move(i, j):
                    child = copy.deepcopy(Board(self))
                    child.make_move(i, j, colour)
                    children.append(child)
        return children

    def victor(self):
        score = 0
        for i in range(8):
            for j in range(8):
                score += self.game_board[i][j]
        return score

    def terminal_state(self):
        for i in range(8):
            for j in range(8):
                if self.valid_move(i, j):
                    return False
        return True

    def print(self):
        r = 1
        for i in range(8):
            if i > 0:
                print(str(r), end=" ")
                r += 1
            for j in range(8):
                if j == 0 and i == 0:
                    print("  0 1 2 3 4 5 6 7")
                    print("0", end=" ")
                if self.game_board[i][j] == 1:
                    print("○", end=" ")
                elif self.game_board[i][j] == -1:
                    print("●", end=" ")
                else:
                    print("-", end=" ")
            print()
        return
