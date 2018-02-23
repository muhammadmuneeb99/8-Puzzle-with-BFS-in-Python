from state import State
import search
import time
import resource


def trace_path(last_pos):
    pos = last_pos.prev
    next_pos = last_pos

    path = []

    while pos != None:
        if pos.node.up() == next_pos.node:
            path.append("Up")
        elif pos.node.down() == next_pos.node:
            path.append("Down")
        elif pos.node.left() == next_pos.node:
            path.append("Left")
        elif pos.node.right() == next_pos.node:
            path.append("Right")

        pos = pos.prev
        next_pos = next_pos.prev

    return path[::-1]


start_time = time.time()
config = [1,2,5,3,4,0,6,7,8]

game = State(config)

result = search.bfs(game)
final_pos = result.position
max_depth = result.max_depth
nodes_expanded = result.nodes_expanded

print("path_to_goal:", trace_path(final_pos))
print("cost_of_path:", final_pos.cost)
print("nodes_expanded:", nodes_expanded)
print("search_depth:", final_pos.depth)
print("max_search_depth:", max_depth)
print("running_time:", time.time() - start_time)
print("max_ram_usage", resource.getrusage(1)[2])
