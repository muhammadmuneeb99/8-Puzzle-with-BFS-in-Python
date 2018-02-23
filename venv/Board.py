class Board:

    def __init__(self, initial_values=[]):
        self.value = initial_values

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(str(self))

    def up(self):
        pos = self.value.index(0)
        if pos in (0, 1, 2):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-3] = new_val[pos-3], new_val[pos]
            return new_val

    def down(self):
        pos = self.value.index(0)
        if pos in (6, 7, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+3] = new_val[pos+3], new_val[pos]
            return new_val

    def left(self):
        pos = self.value.index(0)
        if pos in (0, 3, 6):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos-1] = new_val[pos-1], new_val[pos]
            return new_val

    def right(self):
        pos = self.value.index(0)
        if pos in (2, 5, 8):
            return None
        else:
            new_val = list(self.value)
            new_val[pos], new_val[pos+1] = new_val[pos+1], new_val[pos]
            return new_val