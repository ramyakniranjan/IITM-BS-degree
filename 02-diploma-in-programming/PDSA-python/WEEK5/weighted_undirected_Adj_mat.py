import numpy as np
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
edges = dedges + [(j,i,d) for (i,j,d) in dedges]
WL = np.zeros(shape = (size,size,2))
for (i,j,w) in edges:
    WL[i,j,0] = 1
    WL[i,j,1] = w
print(WL)