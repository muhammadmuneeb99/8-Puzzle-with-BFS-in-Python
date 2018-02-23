from Board import Board
class State:
    """ Handles the state of the game """

    def __init__(self, initial_state=[]):
        self.current = Board(initial_state)

    def __eq__(self, other):
        return self.current == other.current

    def __str__(self):
        return str(self.current)

    def __hash__(self):
        return hash(str(self))

    def up(self):
        up = self.current.up()
        if up is not None:
            return State(up)
        else:
            return self

    def down(self):
        down = self.current.down()
        if down is not None:
            return State(down)
        else:
            return self

    def left(self):
        left = self.current.left()
        if left is not None:
            return State(left)
        else:
            return self

    def right(self):
        right = self.current.right()
        if right is not None:
            return State(right)
        else:
            return self

    def successors(self):
        succ = []

        up = self.current.up()
        if up != None:
            succ.append(State(up))


        down = self.current.down()
        if down != None:
            succ.append(State(down))


        left = self.current.left()
        if left != None:
            succ.append(State(left))


        right = self.current.right()
        if right != None:
            succ.append(State(right))

        return succ