from collections import defaultdict
import heapq
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def createGraph(self,V,edges):
        for edge in edges:
            u,v,weight=edge
            self.graph[u].append((v,weight))

    def display(self):
        for i in range(len(self.graph)+1):
            print(f"{i}:",end=" ")
            for j in (self.graph[i]):
                print(f"{{{j[0]},{j[1]}}}",end=" ")
            print()


    def shortestPath(self,start):
        distances={node: float('infinity') for node in self.graph}
        distances[start]=0

        pq = [(0, start)]  # (distance, node)

     
        while pq:
            current_distance, current_node = heapq.heappop(pq)

        # Skip this node if it has already been processed with a shorter distance
            if current_distance > distances[current_node]:
                continue

        # Explore neighbors
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

            # Only consider this path if it's better than the previously known one
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances


if __name__=="__main__":
    g=Graph()
    edges=[[1,2,10],[1,3,3],[2,3,1],[2,4,2],[3,2,4],[3,4,8],[3,5,2],[4,5,7],[5,4,9]]
    
    g.createGraph(5,edges)
    g.display()
    print(g.shortestPath(1))
    
