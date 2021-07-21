# List the numbers from ascending order to descending

import sys
A=[65,25,12,22,11,4,34,17,18,58]

#Traverse through all array elements
for i in range(len(A)):
    #find the minimum element in remaining unsorted array

    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx = j

    #swap the found minimum element with the first element
    A[i],A[min_idx]=A[min_idx],A[i]

#Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d"%A[i])
