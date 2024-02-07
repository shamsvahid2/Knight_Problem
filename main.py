#import necessary packages
import graphviz
from collections import deque


#all knight possible moves given a location
def possible_moves(x, y):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    return [(x + mx, y + my) for mx, my in moves if 1 <= x + mx <= 8 and 1 <= y + my <= 8]


#(integer, integer) system to (alphabet, integer) system
def position_to_node(x, y):
    return chr(y + ord('a') - 1) + str(x)

#using BFS to find all possible minimal paths
def bfs_all_shortest_paths(start, target):
    queue = deque([[start]])
    shortest_paths = []
    visited = {start: 0}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == target:
            shortest_paths.append(path)
            continue

        for move in possible_moves(*current):
            if move not in visited or visited[move] == len(path):
                visited[move] = len(path)
                queue.append(path + [move])

    return shortest_paths

#using graphviz to draw all paths
def draw_paths(start, end):
    start_pos = (int(start[1]), ord(start[0]) - ord('a') + 1)
    end_pos = (int(end[1]), ord(end[0]) - ord('a') + 1)

    paths = bfs_all_shortest_paths(start_pos, end_pos)
    dot = graphviz.Digraph(comment='Knight Paths', format='png')

    #using different colors for different paths
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'cyan', 'magenta']
    color_index = 0

    for path in paths:
        previous_node = None
        for step, (x, y) in enumerate(path):
            node_label = position_to_node(x, y)
            dot.node(node_label, label=node_label, style='filled', fillcolor='white')
            if previous_node:
                dot.edge(previous_node, node_label, color=colors[color_index], label=str(step))
            previous_node = node_label
        color_index = (color_index + 1) % len(colors)

    dot.render('knight_paths_ordered', view=True)

if __name__ == '__main__':
    #specifying start and end ([alphabet, integer] system)

    # Ask for start and end positions in (letter, number) format
    start_input = input("Please enter the chessboard cell to start from (in 'e2' format): ")
    end_input = input("Please enter the chessboard cell to end at (in 'e4' format): ")


    start = 'a2'
    end = 'h1'
    draw_paths(start_input, end_input)
