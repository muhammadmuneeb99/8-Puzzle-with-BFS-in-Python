from collections import namedtuple


def goal_test(state):
    return str(state) == str(range(0, 9))


# BFS Search
def bfs(start):
    """
    Performs breadth-first search starting with the 'start' as the beginning
    node. Returns a namedtuple 'Success' which contains namedtuple 'position'
    (includes: node, cost, depth, prev), 'max_depth' and 'nodes_expanded'
    if a node that passes the goal test has been found.

    """

    # SearchPos used for bookeeping and finding the path:
    SearchPos = namedtuple('SearchPos', 'node, cost, depth, prev')

    # Initial position does not have a predecessor
    position = SearchPos(start, 0, 0, None)


    # frontier contains unexpanded positions
    frontier = [position]
    explored = set()
    while len(frontier) > 0:

        # current position is the first position in the frontier
        position = frontier.pop(0)

        node = position.node

        # goal test: return success if True
        if goal_test(node):
            max_depth = max([pos.depth for pos in frontier])
            Success = namedtuple('Success',
                        'position, max_depth, nodes_expanded')
            success = Success(position, max_depth, len(explored))
            return success

        # expanded nodes are added to explored set
        explored.add(node)

        # All reachable positions from current postion is added to frontier
        for neighbor in node.successors():
            new_position = SearchPos(neighbor, position.cost + 1,
                                    position.depth + 1, position)
            frontier_check = neighbor in [pos.node for pos in frontier]
            if neighbor not in explored and not frontier_check:
                frontier.append(new_position)

    # the goal could not be reached.
    return None