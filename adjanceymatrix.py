def Create_adj_matrix(V,edges):
    matrix=[[0]* V for _ in range(V)]
    for edge in edges:
        u,v,w=edge
        matrix[u][v]=w
    return matrix

V1=3
edges1=[(0,1,4),(1,2,5),(2,0,7)]
adj_matrix=Create_adj_matrix(V1,edges1)

for row in adj_matrix:
    print(row)
