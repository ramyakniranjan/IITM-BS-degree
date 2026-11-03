#**************************************************************************************************#
#** Unweighted Directed Graph**
#**************************************************************************************************#
import numpy as np
print("Unweighted UnDirected Graph")

# Using numpy 2d array
V = [0,1,2,3,4]
E = [(0,1),(0,2),(1,3),(1,4),(2,4),(2,3),(3,4)]
size = len(V)
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1
print("Adjacency Matrix: ")
print(AMat)

# Using Python nested list
V = [0,1,2,3,4]
E = [(0,1),(0,2),(1,3),(1,4),(2,4),(2,3),(3,4)]
size = len(V)
AMat = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    AMat.append(row.copy())
for i,j in E:
    AMat[i][j] = 1
print("Adjacency list: ")
print(AMat)

# Using python dictionary
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
size = len(V)
AList = {}
for i in range(size):
    AList[i] = []
for (i,j) in E:
    AList[i].append(j)
print("Using python dictionary: ")
print(AList)

#**************************************************************************************************#
#** Unweighted UnDirected Graph**
#**************************************************************************************************#
print("Unweighted UnDirected Graph")

# Using Numpy 2d array
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
UE = E + [(j,i) for (i,j) in E]

size = len(UE)
AMat = np.zeros(shape=(size,size))
for (i,j) in UE:
    AMat[i,j] = 1
print("Using Numpy 2d: ")
print(AMat)

# Using List of lists
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
UE = E + [(j,i) for (i,j) in E]
AMat = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    AMat.append(row.copy())
for(i,j) in UE:
    AMat[i][j] = 1
print("Using List of List: ")
print(AMat)

# Using python dictionary
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
UE = E + [(j,i) for (i,j) in E]
AMat = {}
for i in range(size):
    AMat[i] = []
for (i,j) in UE:
    AMat[j].append(j)
print("Using python dictionary: ")
print(AMat)