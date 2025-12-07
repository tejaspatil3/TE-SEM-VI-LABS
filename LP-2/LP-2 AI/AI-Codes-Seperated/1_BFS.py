from collections import deque

# Sample Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Iterative BFS
def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Recursive BFS
def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    node = queue.popleft()
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs_recursive(graph, queue, visited)

# ▶️ Run Both
start_node = 'A'

print("BFS Iterative:")
bfs_iterative(graph, start_node)

print("\nBFS Recursive:")
visited = set([start_node])
bfs_recursive(graph, deque([start_node]), visited)
