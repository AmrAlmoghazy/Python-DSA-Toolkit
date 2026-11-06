'''Reference:
https://www.geeksforgeeks.org/bubble-sort-algorithm/?ref=gcse_outind
'''

'''Definition:

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
This algorithm is not suitable for large data sets as its average and worst-case time complexity are quite high.

* Time Complexity: O(n^2)
* Space Complexity: O(1)
'''


'''The Algorithm:

1. Start from the first element, compare it with the next element of the array.
2. If the first element is greater than the next element of the array, swap them.
3. Continue this process until the last element.
'''

#* Optimized Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        Is_sorted = True

        # Last i elements are already in place
        for j in range(n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                Is_sorted = False
        
        # If no two elements were Is_sorted in the inner loop, then break
        if Is_sorted:
            break


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:", *arr) # 11 12 22 25 34 64 90


    arr = [1, 2, 3, 4, 5]

    bubbleSort(arr)

    print("Sorted array:", *arr) # 1 2 3 4 5