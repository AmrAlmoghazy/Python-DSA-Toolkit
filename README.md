# Data Structures & Algorithms Toolkit

A structured, educational reference implementation of fundamental computer science algorithms, custom data structures, and asymptotic benchmarks across **Python 3** and **C++**.

---

## Overview

This repository provides clear, self-contained reference implementations of foundational algorithms and data structures. It was created to demonstrate core algorithmic paradigms (divide-and-conquer, recursive decomposition, two-pointer techniques, non-comparison hashing) alongside formal asymptotic time and space complexity analysis.

### Language & Domain Coverage

- **Searching Suite:** Implemented in both **Python 3** and **C++** (7 algorithms each, 14 total).
- **Sorting Suite:** Implemented in **Python 3** (7 algorithms).
- **Custom Data Structures:** Implemented in **Python 3** (Custom `Array` and `SinglyLL`).
- **Empirical Benchmarks:** Implemented in **Python 3** (demonstrating theoretical vs. practical scaling).

---

## Searching Algorithms

Each searching algorithm includes mathematical definitions, complexity analyses, and self-contained execution tests.

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Requires Sorted Array? | Available In |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Linear Search** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | No | Python, C++ |
| **Binary Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ Iterative / $O(\log n)$ Recursive | Yes | Python, C++ |
| **Jump Search** | $O(1)$ | $O(\sqrt{n})$ | $O(\sqrt{n})$ | $O(1)$ | Yes | Python, C++ |
| **Interpolation Search** | $O(1)$ | $O(\log \log n)$ | $O(n)$ | $O(1)$ | Yes (Uniform distribution) | Python, C++ |
| **Exponential Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ Iterative / $O(\log n)$ Recursive | Yes | Python, C++ |
| **Fibonacci Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | Yes | Python, C++ |
| **Ternary Search** | $O(1)$ | $O(\log_3 n)$ | $O(\log_3 n)$ | $O(1)$ Iterative / $O(\log n)$ Recursive | Yes | Python, C++ |

---

## Sorting Algorithms

The sorting suite covers both comparison and non-comparison algorithms, implemented with detailed docstrings, partitioning logic, and test cases.

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? | Key Characteristics |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Optimized with early-exit swap flag |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | In-place minimum extraction |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Adaptive shift-and-insert |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes | Divide-and-conquer recursion |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | No | Lomuto partitioning scheme |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | Max-heap construction & root extraction |
| **Counting Sort** | $O(n + k)$ | $O(n + k)$ | $O(n + k)$ | $O(k)$ | Yes | Non-comparison integer frequency hashing |

*(where $n$ is the number of elements and $k$ is the range of key values).*

---

## Custom Data Structures

### 1. Custom Array (`array_class.py`)
A custom fixed-capacity array data structure illustrating manual memory allocation and Python magic methods:
- `__len__`: Returns the current number of stored elements.
- `__getitem__`: Boundary-checked element retrieval by index.
- `append(value)`: Appends an element if capacity allows.
- `pop()`: Removes and returns the last element.
- `__str__`: Formatted array string representation.

### 2. Singly Linked List (`singly_linked_list.py`)
A pointer-based dynamic data structure featuring:
- **Node Structure:** Encapsulates `data` and `next` pointer references.
- **Insertion Operations:** `insert_at_beginning`, `insert_at_end`, and `insert_at_index`.
- **Deletion Operations:** `delete_at_beginning`, `delete_at_end`, and `delete_at_index`.
- **Search Operations:** Dual implementation providing both iterative traversal and recursive search.
- **Update Operations:** Value replacement (`update_data`) and index-based replacement (`update_idx`).

---

## Asymptotic Benchmarks

Located in the `Benchmarks/` folder:
- **`iterations_calculation.py`:** Simulates nested algorithmic loops over doubling problem sizes ($1,000 \to 16,000$) to observe quadratic iteration growth ($O(n^2)$).
- **`runtime_calculation.py`:** Employs the Python `time` module to measure clock execution time across scaling problem sizes.

---

## Project Structure

```
Python-DSA-Toolkit/
├── .gitignore
├── README.md
├── Benchmarks/
│   ├── iterations_calculation.py
│   └── runtime_calculation.py
├── Data-Structures/
│   └── Python/
│       ├── array_class.py
│       ├── singly_linked_list.py
│       └── sll_testing.py
├── Searching/
│   ├── Cpp/
│   │   ├── binary_search.cpp
│   │   ├── exponential_search.cpp
│   │   ├── fibonacci_search.cpp
│   │   ├── interpolation_search.cpp
│   │   ├── jump_search.cpp
│   │   ├── linear_search.cpp
│   │   └── ternary_search.cpp
│   └── Python/
│       ├── binary_search.py
│       ├── exponential_search.py
│       ├── fibonacci_search.py
│       ├── interpolation_search.py
│       ├── jump_search.py
│       ├── linear_search.py
│       └── ternary_search.py
└── Sorting/
    └── Python/
        ├── bubble_sort.py
        ├── counting_sort.py
        ├── heap_sort.py
        ├── insertion_sort.py
        ├── merge_sort.py
        ├── quick_sort.py
        └── selection_sort.py
```

---

## How to Run

### Prerequisites
- Python 3.8+ (for Python scripts)
- GCC / G++ or Clang with C++11 support (for C++ scripts)

### Running Python Implementations

Run any algorithm directly from the repository root:

```bash
# Searching examples
python Searching/Python/binary_search.py
python Searching/Python/jump_search.py

# Sorting examples
python Sorting/Python/quick_sort.py
python Sorting/Python/merge_sort.py

# Data Structures
python Data-Structures/Python/array_class.py
```

### Compiling and Running C++ Implementations

Compile with standard optimization flags:

```bash
# Example: Binary Search
g++ -O2 Searching/Cpp/binary_search.cpp -o binary_search
./binary_search

# Example: Ternary Search
g++ -O2 Searching/Cpp/ternary_search.cpp -o ternary_search
./ternary_search
```

---

## Testing & Verification

This repository distinguishes between automated assertions and verified manual examples:

1. **Automated Unit Tests (`Data-Structures/Python/sll_testing.py`):**
   - Contains 6 assertion-based test functions specifically verifying the `SinglyLL` implementation:
     - `test_insert_at_beginning()`
     - `test_insert_at_end()`
     - `test_insert_at_index()`
     - `test_delete_at_beginning()`
     - `test_delete_at_end()`
     - `test_delete_at_index()`
   - To execute these tests:
     ```bash
     python -c "import sys; sys.path.append('Data-Structures/Python'); import singly_linked_list; sys.modules['Singly_Linked_list'] = singly_linked_list; import sll_testing; sll_testing.test_insert_at_beginning(); sll_testing.test_insert_at_end(); sll_testing.test_insert_at_index(); sll_testing.test_delete_at_beginning(); sll_testing.test_delete_at_end(); sll_testing.test_delete_at_index(); print('All 6 assertions passed successfully!')"
     ```

2. **Manual & Standalone Verification:**
   - Every searching and sorting implementation includes a self-contained `if __name__ == '__main__':` block with sample inputs (e.g., unsorted lists, target search values) and prints outputs to stdout.
   - Comprehensive automated test frameworks (such as full `pytest` suites covering all permutations) are not claimed or configured.
