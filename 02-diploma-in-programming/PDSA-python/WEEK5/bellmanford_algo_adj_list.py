import numpy as np

def bellmanfordlist(WList,s):
    #Initialization
    infinity  = 1 + len(WList.keys()) * max([d for u in WList.keys() for (v,d) in WList[u]])
    distance = {}
    for v in WList.keys():
        distance[v] = infinity
    distance[s] = 0

    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                if distance[u] + d < distance[v]:
                    distance[v] = distance[u] + d

    return(distance)

edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
size = 8
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))
print(bellmanfordlist(WL,0))


# Time Complexity: O(V * E)
# V: is number of vertices
# E: is number of edges

