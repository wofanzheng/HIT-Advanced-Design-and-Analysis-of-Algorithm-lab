class Block(object):
    def __init__(self, father, kind, g, row, col):
        self.father = father
        self.kind = kind
        self.coordinate_row = row
        self.coordinate_col = col
        self.g = g
        self.f = 0.0

    def get_coordinate(self):
        return self.coordinate_row, self.coordinate_col

    def __lt__(self, other):
        """
        operator <
        :param other:
        :return:
        """
        return self.f < other.f