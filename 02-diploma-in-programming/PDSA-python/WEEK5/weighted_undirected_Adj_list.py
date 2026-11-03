dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,w) in edges:
    WL[i].append((j,w))
print(WL)