from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def create(self,V,edges):
        for edge in edges:
            v1,v2=edge
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
            
    def dfsf(self,start,visited):
        visited.add(start)
        print(start,end=" ")
        for neighbour in self.graph[start]:
            if neighbour not in visited:
                self.dfsf(neighbour,visited)

    def dfspro(self,start):
        visited=set()
        self.dfsf(start,visited)




if __name__ == "__main__":
    V = 6  # Number of vertices
    g=Graph()

    # Define the edges of the graph
    edges = [(1, 5), (1, 4), (4, 6), (3,4), (4, 5),(3,2)]
    g.create(V,edges)

    print("Complete DFS of the graph:")
    g.dfspro(5)  # Perform DFS
