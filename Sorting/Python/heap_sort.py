'''References:
https://www.geeksforgeeks.org/heap-sort/?ref=gcse_outind
https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-heap/?ref=gcse_outind
https://www.geeksforgeeks.org/iterative-heap-sort/?ref=gcse_outind
'''

'''Definition:

Heap sort is a comparison-based sorting technique based on Binary Heap Data Structure.
It can be seen as an optimization over Selection sort, where we first find the max (or min)
element and swap it with the last (or first). We repeat the same process for the remaining elements.
In Heap sort, we use Binary Heap so that we can quickly find and move the max element in O(log n)

* Time Complexity: O(n log n)
* Space Complexity: O(log n) => Recursive call stack
'''

'''The Algorithm:

1. Treat the array as a Complete Binary Tree:
    * The root of the tree is the first element of the array (i = 0).
    * The left child of the node at index i is at index 2*i + 1
    * The right child of the node at index i is at index 2*i + 2
2. Build a Max Heap (heapify):
    * Starting from leaf nodes, compare the parent node with its children
      and ensure that the parent is greater than its children (Swapping).
3. Sort the array by placing the largest element (root) at the end of the array.
    * Swap the root with the last element of the array.
    * Heapify the root element to ensure that the largest element is at the root.
    * Repeat the process for the remaining elements.
'''


# Python program for implementation of Heap Sort

# To heapify a subtree rooted at index i.
def heapify(arr, n, i):

    # Initialize the largest as the root
    largest = i

    # Left child => i = 2*i + 1
    l = 2 * i + 1
    # Right child => i = 2*i + 2
    r = 2 * i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    # If right child is larger than root
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
    

def heapSort(arr):

    n = len(arr)

    # Build a maxheap (rearrange array)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # One by one extract elements
    for i in range(n-1, 0, -1):

        # Move root to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [9, 4, 3, 8, 10, 2, 5]

    heapSort(arr)

    print("Sorted array is:", *arr)   # 2 3 4 5 8 9 10