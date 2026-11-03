def SelectionSort(L): # TC: O(n^2), SC: O(1)
    n = len(L) # len() TC: O(1)
    if n < 1:
        return(L)
    for i in range(n):  # range(n-1)
        # Assume L[:i] is sorted
        mpos = i

        # mpos: position of minimum in L[i]
        for j in range(i+1,n):
            if L[j] < L[mpos]:
                mpos = j

        # L[mpos] is the smallest value in L[i:]
        # Exchange L[mpos] and L[i]
        (L[i], L[mpos]) = (L[mpos],L[i])
        # Now L[:i+1] is sorted
    return(L)
        

# Worst case  complexity is O(n**2);

def StableSelectionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    for i in range(n):
        # Assume the first unsorted element is the minimum
        mpos = i

         # Find the position of the minimum element
        for j in range(i+1,n):
            if L[j] < L[mpos]:
                mpos = j

        # Save the minimum element
        minvalue = L[mpos]

         # Shift elements one position to the right
        while mpos > i:
            L[mpos] = L[mpos - 1]
            mpos -= 1

          # Insert the minimum at position i
        L[i] = minvalue

    return L


def Selection_Sort(array, n):
    
    for i in range(0,n-1):  
        # Assume L[:i] is sorted
        minindex = i

        # mpos: position of minimum in L[i]
        for j in range(i+1,n):
            if array[j] < array[minindex]:
                minindex = j
                
        # L[mpos] is the smallest value in L[i:]
        # Exchange L[mpos] and L[i]
        (array[i], array[minindex]) = (array[minindex], array[i])
        # Now L[:i+1] is sorted
    return(array)


#Time complexity: All versions take O(n^2).
#Auxiliary space: use O(1) extra space.

L=[21,34,8,17,56,72,13,24]
result1 = Selection_Sort(L,8)
print(result1)

result2 = SelectionSort(L)
print(result2)

result3 = StableSelectionSort(L)
print(result3)