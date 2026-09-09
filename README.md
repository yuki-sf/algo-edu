# AlgoEdu

**AlgoEdu** is an educational Python toolkit for learning and exploring classic algorithms.

It provides simple implementations of searching and sorting algorithms along with tools for viewing their source code and learning about their characteristics.

## Features

* Searching algorithms
* Sorting algorithms
* Algorithm complexity information
* Source code inspection
* Simple Python API
* No external runtime dependencies

## Installation

```bash
pip install algo-edu
```

## Usage

### Searching

```python
from algo.search import linear_search, binary_search

numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))
# 2

print(binary_search(numbers, 40))
# 3
```

### Sorting

Sorting functions return a new sorted list without modifying the original list.

```python
from algo.sort import quick_sort, merge_sort

numbers = [5, 2, 8, 1, 3]

print(quick_sort(numbers))
# [1, 2, 3, 5, 8]

print(merge_sort(numbers))
# [1, 2, 3, 5, 8]

print(numbers)
# [5, 2, 8, 1, 3]
```

### View Algorithm Information

Use `algo.info` to explore information about an algorithm.

```python
from algo.info import get_info

info = get_info("quick_sort")

print(info)
```

You can also print formatted information directly:

```python
from algo.info import show_info

show_info("binary_search")
```

### View Source Code

Use `algo.code` to inspect the implementation of an algorithm.

```python
from algo.code import get_code

print(get_code("binary_search"))
```

Or:

```python
from algo.code import show_code

show_code("quick_sort")
```

## Available Algorithms

### Searching

* Linear Search
* Binary Search
* Jump Search
* Interpolation Search
* Exponential Search
* Ternary Search
* Fibonacci Search
* First Occurrence
* Last Occurrence
* Search Range

### Sorting

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Heap Sort
* Counting Sort
* Radix Sort
* Bucket Sort

## Learning-Oriented Design

AlgoEdu is designed with learning in mind.

Alongside the algorithm implementations, the package provides information about:

* Time complexity
* Space complexity
* Stability
* Whether sorted input is required
* Advantages and disadvantages
* Suitable use cases

This makes it useful not only for using algorithms, but also for studying and comparing them.

## Requirements

* Python 3.10 or newer

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
