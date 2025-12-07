# Sample Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# def build_graph():
#     graph = {}
#     n = int(input("Enter number of nodes: "))
#     for _ in range(n):
#         node = input("Enter node: ")
#         neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
#         graph[node] = neighbors
#     return graph

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Recursive DFS
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Iterative DFS
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))  # reverse for consistent order

# # Main Execution
# graph = build_graph()
# start_node = input("Enter start node for DFS: ")

start_node = 'A'

visited1 = set()

dfs(visited1, graph, start_node)

print("\nRecursive DFS:")
dfs_recursive(graph, start_node)

print("\nIterative DFS:")
dfs_iterative(graph, start_node)
