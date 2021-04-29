from collections import defaultdict
class graphBfs:
    def __init__(self):
        self.graphBfs = defaultdict(list)
    def BfsEdge(self,x,y):
        self.graphBfs[x].append(y)
    def bfs(self,a):
        queue=[]
        traversed=[False]*(max(self.graphBfs)+1)

        queue.append(a)
        traversed[a] = True

        while queue:
            a= queue.pop(0)
            print(f"{a}")
             
            for i in self.graphBfs[a]:
                if traversed[i] == False:
                    queue.append(i)
                    traversed[i] = True


b_Graph = graphBfs()
b_Graph.BfsEdge(0,2)
b_Graph.BfsEdge(0,1)
b_Graph.BfsEdge(1,0)
b_Graph.BfsEdge(1,3)
b_Graph.BfsEdge(3,3)
b_Graph.BfsEdge(2,3)

print("Breadth First search for the given graph -> ")
b_Graph.bfs(1)