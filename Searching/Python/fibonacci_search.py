'''Reference:
https://www.geeksforgeeks.org/fibonacci-search/?ref=gcse_outind
'''

'''Definition:

Fibonacci Search is a comparison-based technique 
that uses Fibonacci sequence to search an element in a sorted array.
Fibonacci Search divides given array into unequal parts.

The idea is to first find the smallest Fibonacci number that is greater than or equal to the length of the given array. 
Let the found Fibonacci number be fib (m'th Fibonacci number).
We use (m-2)'th Fibonacci number as the index (If it is a valid index).
Let (m-2)'th Fibonacci Number be i, we compare arr[i] with x, if x is same, we return i.
Else if x is greater, we recurse for subarray after i, else we recurse for subarray before i.

* Time Complexity: O(log n)
* Space Complexity: O(1)
'''


'''The Alogorithm:

1. Find the smallest Fibonacci Number greater than or equal to length of the array and the two numbers before it => (fib_m, fib_m1, fib_m2).
2. Set two indices, offset = -1 and i = fib_m2, which represent the division point of the current search range.
3. Compare x with the value at index i.
4. If x is equal to the value at index i, return i.
5. If x is greater than the value at index i, cut the subarray after i, by moving offset to i, and update i to fib_m1.
6. If x is less than the value at index i, cut the subarray before i, by moving fib_m to fib_m2 and update i to fib_m2.
7. Repeat steps 3-6 until the subarray has only one element.
8. Compare x with the value of the last element of the subarray.
9. If x is equal to the value of the last element, return the index of the last element.
10. If x is not equal to the value of the last element, return -1, indicating that the element is not present in the array.
'''


'''Applications of Fibonacci search:

- It can outperform binary search in scenarios with non-uniform access costs,
  where the Fibonacci sequence helps minimize the number of comparisons.
'''


#* Python program for Fibonacci search

def fibonacci_search(arr, x):

    # Initialize Fibonacci numbers
    fib_m2 = 0                  # (m-2)'th Fibonacci number
    fib_m1 = 1                  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1     # m'th Fibonacci number

    n = len(arr)

    # Finding the smallest Fibonacci number greater than or equal to n
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1     # Marks the eliminated range from front

    # while there are elements to be inspected.
    # Note that we compare arr[fib_m2] with x.
    # When fib_m becomes 1, fib_m2 becomes 0
    while fib_m > 1:
        # Calculate index to compare with x
        i = min(offset + fib_m2, n-1)

        # If x is greater than the value at index i, cut the subarray after i
        if arr[i] < x:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        
        # If x is less than the value at index i, cut the subarray before i
        elif arr[i] > x:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        
        # element found, return index
        else:
            return i
        
    # comparing the last element with x
    if fib_m1 and arr[n-1] == x:
        return n-1
    
    # element not found, return -1
    return -1


arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235]    # len = 12

x = 85
idx = fibonacci_search(arr, x)
if idx > 0:
    print("Found at index:", idx)  # 8
else:
    print(x, "not found")

x = 235
idx = fibonacci_search(arr, x)
if idx > 0:
    print("Found at index:", idx)  # 10
else:
    print(x, "not found")