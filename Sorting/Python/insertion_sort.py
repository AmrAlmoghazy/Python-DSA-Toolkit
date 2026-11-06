'''Reference:
https://www.geeksforgeeks.org/insertion-sort-algorithm/?ref=gcse_outind
'''

'''Definition:

Insertion sort is a simple sorting algorithm that works by iteratively inserting
each element of an unsorted list into its correct position in a sorted portion of the list.
You split the array into two groups: the sorted portion and the unsorted portion.

* Time Complexity: O(n^2)
* Space Complexity: O(1)
'''

'''The Algorithm:

1. Start with second element of the array (as first element is assumed to be sorted).
2. Compare the second element with the first element, if the second is smaller, swap them.
3. Move to the third element and compare it with the first two elements and put at its correct position.
4. Repeat until the entire array is sorted.
'''


#* Python program to implement Insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that're greater than the key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    insertionSort(arr)

    print("Sorted arr:", *arr)