__author__ = 'Shawn Daniel'

from random import randint


class Board(object):

    def __init__(self, board, number, size):
        self.board = board
        self.number = number
        self.size = size

    def build_board(self):
        for item in range(self.size):
            self.board.append(["O"] * self.size)

    def show_board(self):
        print "Board: %d" % self.number
        for row in self.board:
            print ' '.join(row)
        # filter(lambda x: ' '.join(x), self.board)

    def gen_ships(self):
        ship_col = randint(1, len(self.board))
        ship_row = randint(1, len(self.board[0]))
        print "Board %d Ship Column: %d" % (self.number, ship_col)
        print "Board %d Ship Column: %d" % (self.number, ship_row)
        return ship_col, ship_row

    def reset(self):
        del self.board[:]


class Player(object):
    def __init__(self, name, wins, loses):
        self.name = name
        self.wins = wins
        self.loses = loses

    def player_turns(self):
        pass
