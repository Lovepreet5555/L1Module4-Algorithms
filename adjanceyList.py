from collections import defaultdict
def create_adjacencyList(V1,edges):
    adjacencyList =defaultdict(list)
    
    for edge in edges:
        vertex1,vertex2,weight=edge
        adjacencyList[vertex1].append((vertex2,weight))

    for i in range(len(adjacencyList)+1):
        print(f"{i} : ", end=" ")
        for j in (adjacencyList[i]):
            print(f"{{{j[0]},{j[1]}}}", end=" ")
        print()

def main():
    V=3
    edges=[[1, 0, 4],[1, 2, 3],[2, 0, 1]]
    create_adjacencyList(V,edges)

if __name__ =="__main__":
    main()


