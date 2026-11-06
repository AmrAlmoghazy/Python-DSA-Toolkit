'''Reference:
https://www.geeksforgeeks.org/binary-search/?ref=gcse_outind
'''

'''Definition:

Binary Search Algorithm is a searching algorithm used in a sorted array
by repeatedly dividing the search interval in half.

The idea of binary search is to use the information that the array is sorted and reduce the time complexity.

* Time Complexity: O(log n)
* Space Complexity: O(1) => Iterative | O(log n) => Recursive
'''

'''The Algorithm:

1. Divide the search interval into two halves by calculating the middle index.
2. Compare the middle element with the target value.
3. If the target value matches the middle element, return the index.
4. If the target value is less than the middle element, repeat the search on the left subarray.
5. If the target value is greater than the middle element, repeat the search on the right subarray.
6. Repeat the process until the target value is found or the search interval is empty.
7. If the search interval is empty, return -1.
'''

#* Python3 code to implement iterative Binary Searching

# Returns location of x in given array arr
def binarySearch(arr, x):

    low, high = 0, len(arr)-1
    while low <= high:

        # mid = low + (high - low) // 2
        mid = (low + high) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore right half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore left half
        else:
            high = mid - 1

    # If we reach here, then the element is not exist in the array
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is found at index:", result)
    else:
        print("Element is not found.")

#! ========================================================================

#* Python3 program for recursive Binary Searching
# Recursive code animation: https://recursion.vercel.app/

# Returns index of x in arr if present, else -1
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        # mid = low + (high - low) // 2
        mid = (low + high) // 2

        # If element is present at the middle
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid+1, high, x)

    # Element is not present in the array
    else:
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
