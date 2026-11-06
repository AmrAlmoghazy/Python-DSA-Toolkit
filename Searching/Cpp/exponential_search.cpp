#include <bits/stdc++.h>
using namespace std;

//* C++ program to implement Exponential search using recursive Binary search

int binarySearch(int arr[], int, int, int);

// Returns position of first occurrence of x in array
int exponentialSearch(int arr[], int n, int x)
{
	// If x is present at first location itself
	if (arr[0] == x)
		return 0;

	// Find range for binary search by repeated doubling
	int i = 1;
	while (i < n && arr[i] < x)
		i *= 2;

	// Call binary search for the found range.
	return binarySearch(arr, i/2, min(i, n-1), x);
}

// A recursive binary search function.
int binarySearch(int arr[], int l, int r, int x)
{
	if (r >= l)
	{
		int mid = l + (r - l)/2;

		if (arr[mid] == x)
			return mid;

		if (arr[mid] > x)
			return binarySearch(arr, l, mid-1, x);

		return binarySearch(arr, mid+1, r, x);
	}

	return -1;
}

//! ==================================================================

//* Iterative Exponential search implementation

int exponentialSearch(vector<int> arr, int x)
{
    int n = arr.size();
     
    if(n == 0)
        return -1;
 
    // Find range for binary search by repeatedly doubling i
    int i = 1;
    while(i < n and arr[i] < x)
        i *= 2;
 
    // Perform binary search on the range [i/2, min(i, n-1)]
    int l = i/2;
    int r = min(i, n-1);
 
    while(l <= r)
	{
        int mid = (l+r) / 2;
         
        if(arr[mid] == x)
			return mid;
			
        else if(arr[mid] < x)
			l = mid + 1;

        else
			r = mid - 1;
    }
 
    return -1;
}

int main()
{
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr)/ sizeof(arr[0]);
    int x = 10;

    int result = exponentialSearch(arr, n, x);

    (result == -1)
    ? cout <<"Element is not present in array"
    : cout <<"Element is present at index: " << result;

    return 0;
}