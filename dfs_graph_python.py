from collections import defaultdict
class dfs:
    def __init__(self):
        self.dfs = defaultdict(list)

    def edge(self, x, y):
        self.dfs[x].append(y)

    def dfs_f(self, y, traversed):
        traversed.add(y)
        print(y, end=" ")

        for n in self.dfs[y]:
            if n not in traversed:
                self.dfs_f(n,traversed)

    def depthfirst(self, y):
        traversed = set()
        self.dfs_f(y, traversed)

dg = dfs()
dg.edge(0,2)
dg.edge(0,1)
dg.edge(1,0)
dg.edge(1,3)
dg.edge(3,3)
dg.edge(2,3)

print("DFS TRAVERSAL OF A GRAPH (source node is 0): ")
dg.depthfirst(0)