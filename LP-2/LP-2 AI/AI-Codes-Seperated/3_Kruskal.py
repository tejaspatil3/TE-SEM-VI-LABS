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

def kruskal_mst(edges, n):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])
    #key=lambda x: x[2] tells the sort() function to use the weight of each edge as the sorting criterion.
   
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Define edges (u, v, weight)
edges = [
    (0, 2, 3),
    (0, 3, 5),
    (1, 2, 6),
    (1, 4, 9),
    (2, 4, 7),
    (2, 5, 2),
    (3, 5, 8),
    (3, 6, 4),
    (4, 6, 1),
    (5, 6, 3),
    (5, 7, 6),
    (6, 7, 5),
    (6, 8, 7),
    (7, 8, 4)
]


n = 9  # Number of vertices (0 to 8)

mst, total_weight = kruskal_mst(edges, n)

print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")

print(f"Total weight of MST: {total_weight}")