import sys

def prim_mst(graph):
    num_nodes = len(graph)
    selected = [False] * num_nodes
    selected[0] = True  # Start from node 0

    total_weight = 0  # Variable to accumulate the total weight of MST
    print("Edge \tWeight")

    for a in range(num_nodes - 1):
        min_weight = sys.maxsize   #This is a constant in Python that represents the largest integer value
        x = y = 0

        for i in range(num_nodes):
            if selected[i]:
                for j in range(num_nodes):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x, y = i, j

        print(f"{x} - {y} \t{graph[x][y]}")
        total_weight += graph[x][y]  # Add the edge weight to the total weight
        selected[y] = True

    print(f"Total weight of MST: {total_weight}")


# Example graph (5 nodes)
graph = [
    [0, 2, 0, 6, 0],  # Node 0
    [2, 0, 3, 8, 5],  # Node 1
    [0, 3, 0, 0, 7],  # Node 2
    [6, 8, 0, 0, 9],  # Node 3
    [0, 5, 7, 9, 0]   # Node 4
]



# graph = [
#     [0, 0, 3, 5, 0, 0, 0, 0, 0],  # Node 0
#     [0, 0, 6, 0, 9, 0, 0, 0, 0],  # Node 1
#     [3, 6, 0, 0, 7, 2, 0, 0, 0],  # Node 2
#     [5, 0, 0, 0, 0, 8, 4, 0, 0],  # Node 3
#     [0, 9, 7, 0, 0, 0, 1, 0, 0],  # Node 4
#     [0, 0, 2, 8, 0, 0, 3, 6, 0],  # Node 5
#     [0, 0, 0, 4, 1, 3, 0, 5, 7],  # Node 6
#     [0, 0, 0, 0, 0, 6, 5, 0, 4],  # Node 7
#     [0, 0, 0, 0, 0, 0, 7, 4, 0]   # Node 8
# ]
prim_mst(graph)
