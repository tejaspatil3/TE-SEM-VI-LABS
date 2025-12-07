import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))  # (f, g, node, path)
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("Shortest path:", " -> ".join(path))
            print("Total cost:", g)
            return

        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found.")

# Example graph as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic function (estimated cost to goal 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 3,
    'G': 0
}

# Run A*
a_star(graph, 'A', 'G', heuristic)
