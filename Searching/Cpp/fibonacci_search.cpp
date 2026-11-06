//* C++ program to implement Fibonacci search

#include <bits/stdc++.h>
using namespace std;

// Utility function to find minimum of two elements
int min(int x, int y) { return (x<=y) ? x : y; }

int fibonacciSearch(int arr[], int n, int x)
{
    // Initialize fibonacci numbers
    int fib_m2 = 0;                  // (m-2)'th Fibonacci No.
    int fib_m1 = 1;                  // (m-1)'th Fibonacci No.
    int fib_m = fib_m2 + fib_m1;     // m'th Fibonacci No.

    // Finding the first Fib. num greater than or equal to n
    while (fib_m < n)
    {
        fib_m2 = fib_m1;
        fib_m1 = fib_m;
        fib_m = fib_m2 + fib_m1;
    }

    // Marks the eliminated range from front
    int offset = -1;

    /* while there are elements to be inspected. Note that
       we compare arr[fibMm2] with x. When fibM becomes 1,
       fibMm2 becomes 0 */
    while (fib_m > 1)
    {
        // Check if fib_m2 is a valid location
        int i = min(offset + fib_m2, n-1);

        /* If x is greater than the value at index fib_m2,
           cut the subarray array from offset to i */
        if (arr[i] < x)
        {
            fib_m  = fib_m1;
            fib_m1 = fib_m2;
            fib_m2 = fib_m - fib_m1;
            offset = i;
        }

        /* If x is less than the value at index fib_m2,
           cut the subarray after i+1 */
        else if (arr[i] > x)
        {
            fib_m  = fib_m2;
            fib_m1 = fib_m1 - fib_m2;
            fib_m2 = fib_m - fib_m1;
        }

        // element found, return index
        else
            return i;
    }

    // Compare the last element with x
    if (fib_m1 && arr[offset+1] == x)
        return offset + 1;
    
    // element not found, return -1
    return -1;
}

int main()
{
    int arr[] = { 10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 235;
    
    int ind = fibonacciSearch(arr, n, x);
    
    if(ind>=0)
        cout << "Found at index: " << ind;
    else
        cout << x << " isn't present in the array";

    return 0;
}