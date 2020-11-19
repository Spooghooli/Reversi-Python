class Move:

    def __init__(self, row=None, col=None, val=None):
        self.row = -1
        self.col = -1
        self.val = 0

        if row != None and col != None and val!= None:
            self.row = row
            self.col = col
            self.val = val
        elif val != None:
            self.row = -1
            self.col = -1
            self.val = val

    def get_row(self):

        return self.row

    def get_col(self):

        return self.col

    def get_val(self):

        return self.val

    def set_row(self, row):

        self.row = row

    def set_col(self, col):

        self.col = col

    def set_val(self, val):

        self.val = val

