'''Reference:
https://www.geeksforgeeks.org/merge-sort/?ref=gcse_outind
'''

'''Definition:
Merge sort is a Divide-and-Conquer algorithm known for its efficiency and stability..
Works by recursively dividing the input array into two smaller subarrays,
and sorting each of them, then merging them back to obtain a sorted array.

* Time Complexity: O(n log n)
* Space Complexity: O(n)
'''


'''The Algorithm:

1. Divide: divide the array recursively into two halves until it can no longer be divided.
2. Conquer: sort each subarray individually.
3. Merge: merge the sorted subarrays back together in a sorted order.

'''


'''Applications of Merge sort:

- Sorting large datasets.
- External sorting (when data is too large to fit into memory).
- Sorting linked lists.
'''


# Python program for implementation of Merge Sort

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    i = 0       # Initial index of first subarray
    j = 0       # Initial index of second subarray
    k = left    # Initial index of merged subarray

    # Merge the temp arrays back into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    n = len(arr)

    merge_sort(arr, 0, n - 1)
    
    print("Sorted array is:", *arr)