'''References:
https://www.geeksforgeeks.org/jump-search/?ref=gcse_outind
https://www.geeksforgeeks.org/what-is-the-difference-between-binary-search-and-jump-search/?ref=gcse_outind
'''

'''Definition:

Jump search is a searching algorithm for sorted arrays (like Binary search).
The basic idea is to check fewer elements (than linear search)
by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

* Time complexity: O(√n)
* Space complexity: O(1)

Note: The worst case will be (n/m + m-1) where n is the length of the array and m is the jump step.
'''

'''The Algorithm:

1. Given an array of size n and an element x to be searched.
2. initialize the jump step as √n.
3. iterate through the array by jumping ahead by jump step, while the element at the current index is less than x.
4. Once the element at the current index is greater than or equal to x, perform a linear search operation from the previous index to the current index.
5. If the element is found, return the index.
6. If the element is not found, return -1.
'''

''' Performance comparison:  Linear search < Jump search < Binary search '''


import math
def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))    # n**.5
    prev = 0

    # Finding the block where the element is present
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))

        # If the previous index is greater than or equal to n, the element is not present in the array
        if prev >= n:
            return -1

    # Performing linear search in the block
    while arr[prev] < x:
        prev += 1

        # If the current index is equal to the minimum of step and n, the element is not present in the array
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev

    return -1

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 233

idx = jump_search(arr, x)

if idx != -1:
    print(f"Element found at index: {idx}")
else:
    print("Element not found")