# Disjoint Set (Union-Find) Class
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        self.parent[yroot] = xroot
        return True

# Kruskal's Algorithm Function
def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Example Graph: (u, v, weight)
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

n = 4  # Number of vertices (0 to 3)

# Run Kruskal's Algorithm
mst, total_weight = kruskal_mst(edges, n)

# Print the result
print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")

print(f"Total weight of MST: {total_weight}")
