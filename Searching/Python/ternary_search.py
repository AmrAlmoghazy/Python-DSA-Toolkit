'''Reference:
https://www.geeksforgeeks.org/ternary-search/?ref=gcse_outind
'''

'''Definition:

Ternary search is a divide-and-conquer algorithm
that operates on the priciple of dividing the sorted array into three equal segments (instead of two as in binary search),
and determine in which segment the key element is located.
The basic idea is to narrow down the search space by comparing the target value with elements
at two points that divide the array into three equal parts:
mid1 = l + (r-l) / 3
mid2 = r - (r-l) / 3

* Time Complexity: O(2*log3(n))
* Space Complexity: O(log3(n)) => Recursive || O(1) => Iterative
'''


'''The Algorithm:

1. Set l,r (Two pointers initially pointing to first and last elements).
2. Calculate mid1 = left + (right - left) / 3 and mid2 = right - (right - left) / 3,
   to divide the current search space into three equal parts: [left, mid1], [mid1, mid2], [mid2, right].
3. Compare the key element with mid1 & mid2, if key found, return the index.
4. If the key is less than mid1, update the right pointer to mid1 - 1,
   If the key is greater than mid2, updata the left pointer to mid2 + 1,
   Otherwise, the key is between mid1 & mid2, then update the left to mid1 + 1 and the right to mid2 - 1.
5. Repeat the process until the key element is found, return it's index.
   Or the search space becomes empty, return -1. 
'''


'''Applications of Ternary search:

- Finding position of specific value in a large sorted array.
- Finding the maximum or minimum value of a function.
- Finding bitonic point in a bitonic sequence.
- Evaluating a quadratic expression.
'''


# #* Python program to implement ternary search using recursion

# import math

# # Function to perform Ternary Search
# def ternarySearch(arr, l, r, key):

#     if (r >= l):

#         # Find the mid1 and mid2
#         mid1 = l + (r - l) // 3
#         mid2 = r - (r - l) // 3

#         # Check if key is present at any mid
#         if (arr[mid1] == key): 
#             return mid1
        
#         if (arr[mid2] == key): 
#             return mid2
        
#         # Since key is not present at mid,
#         # check in which region it is present
#         # then repeat the Search operation in that region
#         if (key < arr[mid1]): 

#             # The key lies in between l and mid1
#             return ternarySearch(arr, l, mid1 - 1, key)
        
#         elif (key > arr[mid2]):

#             # The key lies in between mid2 and r
#             return ternarySearch(arr, mid2 + 1, r, key)
        
#         else: 

#             # The key lies in between mid1 and mid2
#             return ternarySearch(arr, mid1 + 1, mid2 - 1, key)
        
#     # Key not found
#     return -1



# a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# l = 0
# r = len(a)-1

# key = 5
# p = ternarySearch(a, l, r, key)
# print("Index of", key, "is", p)

# key = 50
# p = ternarySearch(a, l, r, key)
# print("Index of", key, "is", p)


#! ====================================================================


# Python program to illustrate iterative approach to ternary search

# Function to perform Ternary Search
def ternarySearch(arr, key):
    l = 0
    r = len(arr) - 1

    while r >= l:

        # Find mid1 and mid2
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3

        # Check if key is at any mid
        if key == arr[mid1]:
            return mid1
        if key == arr[mid2]:
            return mid2

        # Since key is not present at mid, 
        # Check in which region it is present
        # Then repeat the search operation in that region
        if key < arr[mid1]:
            # key lies between l and mid1 (left part)
            r = mid1 - 1

        elif key > arr[mid2]:
            # key lies between mid2 and r (right part)
            l = mid2 + 1

        else:
            # key lies between mid1 and mid2
            l = mid1 + 1
            r = mid2 - 1

    # key not found
    return -1



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

key = 5
p = ternarySearch(a, key)
print("Index of", key, "is", p)

key = 50
p = ternarySearch(a, key)
print("Index of", key, "is", p)