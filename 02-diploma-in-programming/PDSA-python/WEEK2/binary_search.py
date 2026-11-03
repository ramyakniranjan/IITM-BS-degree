# Iterative Implementation
def binary_search(L,v):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low + high) // 2
        if L[mid] > v:
            high = mid - 1
        elif L[mid] < v:
            low = mid + 1
        else:
            return mid
    return False

# Recursive Implementation with slicing
def binarySearch(l,v):
    if l == []:
        return(False)
    
    m = len(l)//2

    if v == l[m]:
        return(True)

    if v < l[m]:
        return(binarySearch(l[:m], v))
    else:
        return(binarySearch(l[m+1:], v))


def bsearch(l,v):
    if l == []:
        return(False)

    m = len(l)//2

    if v == l[m]:
        return(True)

    if v < l[m]:
        return(bsearch(l[:m], v))
    else:
        return(bsearch(l[m+1:], v))

# Recurrsive Implementation without slicing
def Binary_Search(L, v, left = 0, right=None):
    if right is None:
        right  = len(L) - 1

    if left > right:
        return -1
    
    mid = (left + right) // 2

    if v == L[mid]:
        return mid
    elif v > L[mid]:
        return Binary_Search(L,v, mid + 1, right)
    else: 
        return Binary_Search(L,v,left, mid - 1)




# Sorted list: time complexity O(1) (bestcase); O(logn) (worstcase)
# Unsorted list: time complexity O(n) (worstcase); 

L = [1,3,4,5,6,8]
v = 6
print(f"binary_search: {binary_search(L,v)}")
print(f"binarySearch: {binarySearch(L,v)}")
print(f"bsearch: {bsearch(L,v)}")
print(f"bsearch: {Binary_Search(L,v)}")