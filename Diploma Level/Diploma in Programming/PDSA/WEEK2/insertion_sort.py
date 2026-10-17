# Iterative
def InsertionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        j = i
        while(j>0 and L[j] < L[j-1]):
            (L[j], L[j-1]) = (L[j-1],L[j])
            j = j - 1
    return L


# Recursive
def Insert(L,v):
    n = len(L)
    if n == 0:
        return([v])
    if v >= L[-1]:
        return (L+[v])
    else:
        return(Insert(L[:-1],v)+L[-1:])
    
def ISort(L):
    n = len(L)
    if n < 1:
        return(L)
    L = Insert(ISort(L[:-1]),L[-1])
    return(L)

L=[21,34,8,17,56,72,13,24]
result = InsertionSort(L)
print(result)

result = ISort(L)
print(result)
