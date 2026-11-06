'''Reference:
https://www.geeksforgeeks.org/counting-sort/?ref=gcse_outind
'''

'''Definition:

Counting Sort is a non-comparison-based sorting algorithm.
It is particularly efficient when the range of input values is small compared to the number of elements to be sorted.
The basic idea behind Counting Sort is to count the frequency of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

* Time Complexity: O(n+k) where n is the number of elements in the input array and k is the range of input.
* Space Complexity: O(n+k)
'''


'''The Algorithm:

1. Find out the maximum element in the array (to find the range of input elements).
2. Initialize a count array of length max+1 with zeros (frequency array).
3. Store the count of each element in the input array.
4. Apply prefix sum on the count array (countArray[i] += countArray[i-1]).
   * This will help in placing the elements of the input array at the correct index in the output array. 
5. Create an output array of the same length as the input array.
6. Iterate from end of the input array and because traversing input array from end preserves the order of equal elements, which eventually makes this sorting algorithm stable.
   * Update: outputArray[countArray[inputArray[i]] - 1] = inputArray[i]
   * Decrement the countArray[inputArray[i]] by 1.
'''


def counting_sort(inputArray):
    L = len(inputArray)

    # Finding the maximum element in the input array
    M = max(inputArray)

    # Initializing the count array with zeros
    countArray = [0] * (M + 1)

    # Storing the count of each element in the input array
    for i in inputArray:
        countArray[i] += 1
    
    # Applying prefix sum on the count array
    for i in range(1, M + 1):
        countArray[i] += countArray[i-1]
    
    # Creating an output array of the same length as the input array
    outputArray = [0] * L

    # Iterating from end of the input array
    for i in range(L-1, -1, -1):
        outputArray[countArray[inputArray[i]] - 1] = inputArray[i]
        countArray[inputArray[i]] -= 1
    
    return outputArray


if __name__ == '__main__':
    arr = [2, 5, 3, 0, 2, 3, 0, 3]

    print("Sorted array is:", *counting_sort(arr))
