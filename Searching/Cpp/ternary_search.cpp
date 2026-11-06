#include <bits/stdc++.h>
using namespace std;

//* C++ program to illustrate recursive approach to ternary search

// A function to perform Ternary Search
int ternarySearch(int arr[], int l, int r, int key)
{
    if (r >= l)
    {
        // Find the mid1 and mid2
        int mid1 = l + (r - l) / 3;
        int mid2 = r - (r - l) / 3;

        // Check if key is present at any mid
        if (arr[mid1] == key) return mid1;
        if (arr[mid2] == key) return mid2;

        // Since key is not present at mid,
        // check in which region it is present
        // then repeat the Search operation in that region
        if (key < arr[mid1])
        {
            // The key lies in between l and mid1
            return ternarySearch(arr, l, mid1 - 1, key);
        }

        else if (key > arr[mid2]) 
        {
            // The key lies in between mid2 and r
            return ternarySearch(arr, mid2 + 1, r, key);
        }

        else 
        {
            // The key lies in between mid1 and mid2
            return ternarySearch(arr, mid1 + 1, mid2 - 1, key);
        }
    }

    // Key not found
    return -1;
}

//! =======================================================================

//* C++ program to illustrate iterative approach to ternary search

// Function to perform Ternary Search
int TernarySearch(int arr[], int l, int r, int key)
{
    while (r >= l) 
    {
        // Find the mid1 and mid2
        int mid1 = l + (r - l) / 3;
        int mid2 = r - (r - l) / 3;

        // Check if key is present at any mid
        if (arr[mid1] == key) return mid1;
        if (arr[mid2] == key) return mid2;

        // Since key is not present at mid,
        // check in which region it is present
        // then repeat the Search operation in that region
        if (key < arr[mid1]) 
        {
            // The key lies in between l and mid1
            r = mid1 - 1;
        }

        else if (key > arr[mid2]) 
        {
            // The key lies in between mid2 and r
            l = mid2 + 1;
        }

        else
        {
            // The key lies in between mid1 and mid2
            l = mid1 + 1;
            r = mid2 - 1;
        }
    }

    // Key not found
    return -1;
}


int main()
{
    int l, r, p, key;

    int a[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    l = 0;
    r = 9;

    key = 5;
    p = ternarySearch(a, l, r, key);
    cout << "Index of " << key << " is " << p << endl;

    key = 50;
    p = TernarySearch(a, l, r, key);
    cout << "Index of " << key << " is " << p << endl;
}