'''References:
https://www.geeksforgeeks.org/linear-search/?ref=gcse_outind
https://www.geeksforgeeks.org/what-is-linear-search/?ref=gcse_outind
'''

'''Definition:

The linear search algorithm is defined as a sequential search algorithm
that starts at one end and goes through each element of a list until the desired element is found;
otherwise, the search continues till the end of the dataset.

* Time Complexity: O(n)
* Space Complexity: O(1)
'''

'''The Algorithm:

1. Start: begin at the first element of the collection of elements.
2. Compare: compare the current element to the desired element.
3. Found: if the current element is equal to the desired element, return true or the index of the current element.
4. Move: Otherwise, move to the next element.
5. Repeat: Repeat steps 2-4 until the desired element is found or the end of the collection is reached.
6. End: If the end of the collection is reached, return false or -1.
'''

'''Applications of linear search:

- Unsorted lists
- Small datasets
- Searching linked lists
- Simple implementation
'''

# Python3 code to linearly search x in arr[].
def search(arr, N, x):
    for i in range(N):
        if (arr[i] == x):
            return i
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    result = search(arr, N, x)
    if(result == -1):
        print("Element not found.")
    else:
        print("Element is present at index:", result)