from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_traversal(self):
        visited = [False] * self.V
        print("\nDFS Traversal:")
        for i in range(self.V):
            if not visited[i]:
                self._dfs_util(i, visited)

    def _dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

    def bfs_traversal(self):
        visited = [False] * self.V
        print("\nBFS Traversal:")
        for i in range(self.V):
            if not visited[i]:
                self._bfs_util(i, visited)

    def _bfs_util(self, start, visited):
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dfs_recursive_search(self, target):
        visited = [False] * self.V
        path = []

        for i in range(self.V):
            if not visited[i]:
                if self._dfs_search_util(i, visited, path, target):
                    print("\nDFS Recursive Search:")
                    print("Vertex Found")
                    print("Path:", ' -> '.join(map(str, path)))
                    return
        print("\nDFS Recursive Search:")
        print("Vertex Not Found")

    def _dfs_search_util(self, node, visited, path, target):
        visited[node] = True
        path.append(node)
        if node == target:
            return True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self._dfs_search_util(neighbor, visited, path, target):
                    return True
        path.pop()
        return False

    def bfs_recursive_search(self, target):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                found, path = self._bfs_recursive_util([i], visited, target, [])
                if found:
                    print("\nBFS Recursive Search:")
                    print("Vertex Found")
                    print("Path:", ' -> '.join(map(str, path)))
                    return
        print("\nBFS Recursive Search:")
        print("Vertex Not Found")

    def _bfs_recursive_util(self, queue, visited, target, path):
        if not queue:
            return False, []
        next_queue = []
        for node in queue:
            if visited[node]:
                continue
            visited[node] = True
            path.append(node)
            if node == target:
                return True, path
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    next_queue.append(neighbor)
        return self._bfs_recursive_util(next_queue, visited, target, path)


if __name__ == "__main__":
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    g = Graph(v)
    print("Enter edges (pairs of vertices):")
    for _ in range(e):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    g.dfs_traversal()
    g.bfs_traversal()

    while True:
        print("\nSearch Menu:")
        print("1. DFS Recursive Search")
        print("2. BFS Recursive Search")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '3':
            break
        vertex = int(input("Enter vertex to search for: "))

        if choice == '1':
            g.dfs_recursive_search(vertex)
        elif choice == '2':
            g.bfs_recursive_search(vertex)
        else:
            print("Invalid choice. Try again.")

