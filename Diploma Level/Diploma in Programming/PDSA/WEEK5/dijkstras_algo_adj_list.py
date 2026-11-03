def dijkstralist(WList,s):
    #Initialization
    infinity = 1 + len(WList.keys()) * max([d for u in WList.keys() for (v,d) in WList[u]])
    (visited, distance) = ({}, {})
    for v in WList.keys():
        (visited[v], distance[v]) = (False, infinity)
    distance[s] = 0

    # Computing shortest distance from each vertex from source

    for u in WList.keys():
        min_dist = min([distance[v] for v in WList.keys() if not visited[v]])

        nextv_list = [v for v in WList.keys() if (not visited[v] and distance[v] == min_dist)]

        nextv = min(nextv_list)
        visited[nextv] = True

        for (v,d) in WList[nextv]:
            if not visited[v]:
                if distance[nextv] + d < distance[v]:
                    distance[v] = distance[nextv] + d
    return(distance)


dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in dedges:
    WL[i].append((j,d))
print(dijkstralist(WL,0))
