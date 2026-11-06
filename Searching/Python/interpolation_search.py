'''References:
https://www.geeksforgeeks.org/interpolation-search/?ref=gcse_outind
'''

'''Definition:

The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed.
This search algorithm works on the probing position of the required value.
This algorithm works on the principle of linear interpolation.
Interpolation constructs new data points within the range of a discrete set of known data points.
Interpolation search may go to different locations according to the value of the key being searched.

** Finding Position to be searched **
pos = low + [ (x-arr[low])*(high-low) / (arr[high]-arr[low]) ]

where:
arr[] => Array where elements need to be searched
x     => Element to be searched
low   => Starting index in arr[]
high  => Ending index in arr[]

Note: The idea of the formula is to return higher value when x is closer to arr[high],
      and smaller value when x is closer to arr[low].


* Time Complexity: θ(log(log(n))) if the elements are uniformly distributed, O(n) in the worst case.
* Space Complexity: O(1)
'''

'''The Algorithm:

1. In a loop, calculate the 'pos' using the probability position formula.
2. If it's a match, return the index of the element.
3. If the element is less than arr[pos], calculate the prob. position of the left sub-array.
   Otherwise, calculate the same in the right sub-array.
4. Repeat until a match is found or the sub-array reduces to zero, return -1.
'''


#* Python3 program to implement iterpolation search using recursion

def interpolationSearch(arr, lo, hi, x):

    # An element in the array must be in range defined by corner (as it's sorted)
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):

		# Probing the position with keeping uniform distribution in mind.
		pos = lo + ( (hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]) )

		# Condition of target found
		if arr[pos] == x:
			return pos

		# If x is larger, x is in right subarray
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1, hi, x)

		# If x is smaller, x is in left subarray
		if arr[pos] > x:
			return interpolationSearch(arr, lo, pos - 1, x)

	return -1


arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr)
x = 18

index = interpolationSearch(arr, 0, n-1, x)

if index != -1:
	print("Element found at index:", index)
else:
	print("Element not found")
	

#! ============================================================================


#* Python program to implement interpolation search by using iteration approach

def interpolationSearch(arr, n, x): 

	# Find indexes of two corners 
	low = 0
	high = (n - 1) 

	while low <= high and x >= arr[low] and x <= arr[high]:
		 
		if low == high:
			
			if arr[low] == x: 
				return low; 
		
			return -1; 

		pos = int(low + ( ((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])) ))
		# pos = low + (high - low) // (arr[high] - arr[low]) * (x - arr[low])
		
		# Condition of target found 
		if arr[pos] == x: 
			return pos 

		# If x is larger, x is in upper part 
		if arr[pos] < x: 
			low = pos + 1 

		# If x is smaller, x is in lower part 
		else: 
			high = pos - 1
	
	return -1

if __name__ == "__main__":
	
	arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
	n = len(arr) 
	x = 18

	index = interpolationSearch(arr, n, x) 

	if index != -1: 
		print ("Element found at index:",index)
	else: 
		print ("Element not found")