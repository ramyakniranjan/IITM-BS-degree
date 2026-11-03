def quicksort(L,l,r):
    if (r - 1 <= 1):
        return L
    (pivot, lower, upper) = (L(l), l+1, l+1)
    for i in range(l+1,r):
        if L[i] > pivot:
            upper = upper + 1.                        
        else:
            (L[i], L[lower]) = (L[lower], L[i])
            (lower, upper) = (lower+1, upper+1)
    (L[l], L[lower - 1]) = (L[lower - 1], L[l])
    lower = lower - 1
    quicksort(L,l,lower)
    quicksort(L,lower+i,upper)
    return(L)


# Time Complexity: 
# best_case: O(nlogn)
# worst_case: O(n^2)
# average_case: O(nlogn)

# Space Complexity:
# Stack_max_size:
    #worst_case: n
    #best_case: logn