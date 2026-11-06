'''Reference:
https://www.geeksforgeeks.org/quick-sort-algorithm/?ref=gcse_outind
https://www.geeksforgeeks.org/quick-sort-vs-merge-sort/?ref=gcse_outind
'''

'''Definition:

QuickSort is a Divide and Conquer algorithm.
that picks an element as pivot and partitions the given array around the picked pivot.
by placing the pivot in its correct position in the sorted array.

* Time Complexity: O(n^2) in worst case, O(n log n) in average case
* Space Complexity: O(n) => recursive call stack
'''

'''The Algorithm:

1. Pick a Pivot: select an element as the pivot (the choice of pivot can vary).
2. Partition the array: reorder the array around the pivot. After partitioning,
   all elements smaller than the pivot are on the left side of the pivot, and all
   elements greater than the pivot are on the right side of the pivot, then
   the pivot is in its correct position.
3. Recursively call: apply the same process to the two positioned sub-arrays (left & right of the pivot).
4. Base case: the recursion stops when there is only one element in the sub-array (a single element is already sorted).


** Approaches of choosing the Pivot:

- Picking the first (or last) element as the pivot: The problem with this approach is it ends up with the worst-case when the array is already sorted.
- Picking a random element as the pivot: This approach is better than the first one (doesn't have a pattern for worst case), but it is not the best.
- Picking the median element as the pivot: This is the best approach (as it will always divide the array into two halves),
  but it is not practical because it requires finding the median element which is time-consuming.


** Partitioning the array (3 common algorithms):

- Naive Partition: we create two empty arrays (left and right) and iterate over the array to fill them.
- Lomuto Partition: we start from the left side of the array and keep track of the index of the elements smaller than or equal the pivot (*).
- Hoare's Partition: we start from both sides of the array and iterate over it to find the elements less than and greater than the pivot (The fastest one).
'''

'''Applications of QuickSort:

- Efficiently sorting large datasets.
- QuickSort is used in the C standard library for sorting arrays of data and many other programming laguages (e.g. Java).
- Used in the Unix operating system for sorting files.
- Used in the database management system for sorting records.
- Applied in cryptography for generating random permutations and unpredictable encyption keys.
'''

# Quick Sort Algorithm

# Partitioning the array using Lomuto's Partition
def partition(arr, low, high):

    # Choose the pivot (last element)
    pivot = arr[high]

    # Index of the smaller element and indicates the right position of the pivot.
    i = low - 1

    # Iterate over the array and swap the elements to reorder them around the pivot.
    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place the pivot in its correct position
    arr[i+1], arr[high] = arr[high], arr[i+1]

    # return the index of the pivot
    return i + 1


# Quick Sort implementation
def quickSort(arr, low, high):
    
        if low < high:
    
            # Partition the array
            pi = partition(arr, low, high)
    
            # Recursively call the function for the left and right sub-arrays
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quickSort(arr, 0, n-1)
    
    print("Sorted array is:", *arr)



'''

def QuickSort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[-1]
    L = QuickSort([x for x in arr[:-1] if x <= pivot])
    R = QuickSort([x for x in arr[:-1] if x > pivot])
    return L + [pivot] + R

'''