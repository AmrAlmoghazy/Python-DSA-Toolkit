'''Reference:
https://www.geeksforgeeks.org/exponential-search/?ref=gcse_outind
'''

'''Definition:

It's name comes from the way it searches an element.
Exponential search works on sorted array.
It involves two steps: 1. Finding range where element exist  2. Doing Binary search on that range
To find the range required, start with subarray of size 1, compare its last element with x,
then try size 2, and so on until the last element in the subarray is greater than x.

* Time Complexity: O(log n)
* Space Complexity: Recursive Binary search requires O(log n), while iterative Binary search requires only O(1) 
'''

'''The Algorithm:

1. If x occurs in the first element, return 0.
2. Else, begin with index 1 and check if the last element in the subarray is greater than or equal x.
3. Repeat doubling the size of the subarray until the last element is greater than or equal x.
4. Perform Binary search on the subarray from index i/2 to min(i,n-1) to find the position of x.
5. If x not found, return -1.
'''

'''Applications of Exponential search: 

- Exponential Binary Search is particularly useful for unbounded searches, where size of array is infinite.
- It works better than Binary Search for bounded arrays, and also when the element to be searched is closer to the first element.
'''


#* Python program to implement Exponential search 

# # Recursive Binary search function
# def binarySearch(arr, l, r, x):
# 	if r >= l:
# 		mid = l + (r-l) // 2
		
# 		if arr[mid] == x:
# 			return mid
		
# 		if arr[mid] > x:
# 			return binarySearch(arr, l, mid - 1, x)
		
# 		return binarySearch(arr, mid + 1, r, x)
		
# 	return -1


# # Returns the position of first occurrence of x in array
# def ExponentialSearch(arr, n, x):
	
# 	# IF x is present at first location itself
# 	if arr[0] == x:
# 		return 0
		
# 	# Find range for binary search by repeated doubling
# 	i = 1
# 	while i < n and arr[i] < x:
# 		i *= 2
	
# 	# Call binary search for the found range
# 	return binarySearch(arr, i//2, min(i, n-1), x)
	

# arr = [2, 3, 4, 10, 40]
# n = len(arr)
# x = 10

# result = ExponentialSearch(arr, n, x)

# if result == -1:
# 	print ("Element not found in the array")
# else:
# 	print ("Element is present at index: %d" %(result))
	

#! ==========================================================================

#* Iterative Exponential search implementation

def exponential_search(arr, x):
	n = len(arr)
	
	if n == 0:
		return -1
	
	# If x is present at first location itself
	if arr[0] == x:		# size = 1
		return 0

	# Find range for binary search by repeatedly doubling i
	i = 1
	while i < n and arr[i] < x:
		i *= 2

	# Perform binary search on the range [i/2, min(i, n-1)]
	left = i // 2
	right = min(i, n-1)

	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			left = mid + 1
		else:
			right = mid - 1

	return -1


arr = [2, 3, 4, 10, 40]
n = len(arr)
x = 10

result = exponential_search(arr, x)

if result == -1:
	print ("Element not found in the array")
else:
	print ("Element is present at index: %d" %(result))