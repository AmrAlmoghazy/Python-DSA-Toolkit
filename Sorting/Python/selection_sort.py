'''Reference:
https://www.geeksforgeeks.org/selection-sort-algorithm-2/?ref=gcse_outind
'''

'''Defenition:

Selection Sort is a comparison-based sorting algorithm.
It sorts an array by repeatedly selecting the smallest (or largest)
element from the unsorted portion and swapping it with the first unsorted element.
This process continues until the entire array is sorted.

* Time Complexity: O(n^2)
* Space Complexity: O(1)
'''

'''The Algorithm:

1. Find the smallest element in the array.
2. Swap it with the first element in unsorted part.
3. Repeat the process for the remaining elements.
'''

#* Python code for Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        # Assume the minimum element is the first element in unsorted portion
        min_idx = i

        # Loop through the unsorted portion of the array
        for j in range(i+1, n):

            if arr[j] < arr[min_idx]:

                # Update min_idx if a smaller element is found
                min_idx = j

        # Swap the minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]

    selection_sort(arr)

    print("Sorted array is:", arr)  # Output: [11, 12, 22, 25, 64]