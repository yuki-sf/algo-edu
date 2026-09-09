_ALGORITHM_INFO = {
    # ==================== SEARCH ====================

    "linear_search": {
        "name": "Linear Search",
        "category": "Search",
        "description": (
            "Searches for a target element by checking each element "
            "sequentially from the beginning."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(n)",
            "worst": "O(n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": False,
        "advantages": [
            "Works on both sorted and unsorted data.",
            "Simple to implement.",
            "Requires no additional data structures.",
        ],
        "disadvantages": [
            "Slow for large datasets.",
            "May need to examine every element.",
        ],
        "best_use_case": "Small or unsorted datasets.",
    },

    "binary_search": {
        "name": "Binary Search",
        "category": "Search",
        "description": (
            "Searches for a target in a sorted list by repeatedly "
            "dividing the search range in half."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Very efficient for large sorted datasets.",
            "Requires constant extra space.",
        ],
        "disadvantages": [
            "Requires the data to be sorted.",
            "Less useful for frequently changing unsorted data.",
        ],
        "best_use_case": "Searching large sorted arrays.",
    },

    "jump_search": {
        "name": "Jump Search",
        "category": "Search",
        "description": (
            "Searches a sorted list by jumping ahead by fixed blocks "
            "and then performing a linear search within the matching block."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(√n)",
            "worst": "O(√n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Faster than linear search on sorted data.",
            "Uses constant extra space.",
        ],
        "disadvantages": [
            "Requires sorted data.",
            "Usually slower than binary search for random-access arrays.",
        ],
        "best_use_case": "Sorted arrays where sequential block access is useful.",
    },

    "interpolation_search": {
        "name": "Interpolation Search",
        "category": "Search",
        "description": (
            "Estimates the likely position of a target based on its value "
            "within a sorted and approximately uniformly distributed dataset."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log log n)",
            "worst": "O(n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Can outperform binary search on uniformly distributed data.",
            "Requires constant extra space.",
        ],
        "disadvantages": [
            "Performance depends heavily on data distribution.",
            "Can degrade to linear time.",
            "Requires sorted numeric data.",
        ],
        "best_use_case": "Large, sorted, uniformly distributed numeric data.",
    },

    "exponential_search": {
        "name": "Exponential Search",
        "category": "Search",
        "description": (
            "Finds a range containing the target by exponentially "
            "increasing the search boundary, then performs binary search."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Efficient for sorted data.",
            "Works well when the target is near the beginning.",
        ],
        "disadvantages": [
            "Requires sorted data.",
            "More complex than ordinary binary search.",
        ],
        "best_use_case": "Sorted datasets where the target may be near the beginning.",
    },

    "ternary_search": {
        "name": "Ternary Search",
        "category": "Search",
        "description": (
            "Searches a sorted list by dividing the search range into "
            "three sections at each step."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Reduces the search range at each iteration.",
            "Uses constant extra space.",
        ],
        "disadvantages": [
            "Usually performs more comparisons than binary search.",
            "Requires sorted data.",
        ],
        "best_use_case": "Educational purposes and specialized search problems.",
    },

    "fibonacci_search": {
        "name": "Fibonacci Search",
        "category": "Search",
        "description": (
            "Searches a sorted list using Fibonacci numbers to divide "
            "the search range into progressively smaller sections."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Requires constant extra space.",
            "Uses simple arithmetic for range calculations.",
        ],
        "disadvantages": [
            "Generally less practical than binary search.",
            "Requires sorted data.",
            "More complicated to implement.",
        ],
        "best_use_case": "Specialized search problems and educational purposes.",
    },

    "first_occurrence": {
        "name": "First Occurrence",
        "category": "Search",
        "description": (
            "Finds the first index at which a target value occurs "
            "in a sorted list."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Efficiently finds the first duplicate occurrence.",
            "Uses constant extra space.",
        ],
        "disadvantages": [
            "Requires sorted data.",
        ],
        "best_use_case": "Finding the starting position of duplicate values.",
    },

    "last_occurrence": {
        "name": "Last Occurrence",
        "category": "Search",
        "description": (
            "Finds the last index at which a target value occurs "
            "in a sorted list."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Efficiently finds the final duplicate occurrence.",
            "Uses constant extra space.",
        ],
        "disadvantages": [
            "Requires sorted data.",
        ],
        "best_use_case": "Finding the ending position of duplicate values.",
    },

    "search_range": {
        "name": "Search Range",
        "category": "Search",
        "description": (
            "Finds the first and last positions of a target value "
            "in a sorted list."
        ),
        "time_complexity": {
            "best": "O(1)",
            "average": "O(log n)",
            "worst": "O(log n)",
        },
        "space_complexity": "O(1)",
        "stable": "Not applicable",
        "requires_sorted": True,
        "advantages": [
            "Finds the complete range of duplicate values efficiently.",
            "Uses constant extra space.",
        ],
        "disadvantages": [
            "Requires sorted data.",
        ],
        "best_use_case": "Finding the range occupied by duplicate values.",
    },

    # ==================== SORT ====================

    "bubble_sort": {
        "name": "Bubble Sort",
        "category": "Sorting",
        "description": (
            "Repeatedly compares adjacent elements and swaps them "
            "when they are in the wrong order."
        ),
        "time_complexity": {
            "best": "O(n)",
            "average": "O(n²)",
            "worst": "O(n²)",
        },
        "space_complexity": "O(n)",
        "stable": True,
        "requires_sorted": False,
        "advantages": [
            "Very simple to understand and implement.",
            "Can detect an already sorted list efficiently.",
            "Stable sorting algorithm.",
        ],
        "disadvantages": [
            "Very slow for large datasets.",
            "Many unnecessary comparisons and swaps.",
        ],
        "best_use_case": "Small datasets and educational purposes.",
    },

    "selection_sort": {
        "name": "Selection Sort",
        "category": "Sorting",
        "description": (
            "Repeatedly finds the smallest remaining element and places "
            "it in its correct position."
        ),
        "time_complexity": {
            "best": "O(n²)",
            "average": "O(n²)",
            "worst": "O(n²)",
        },
        "space_complexity": "O(n)",
        "stable": False,
        "requires_sorted": False,
        "advantages": [
            "Simple implementation.",
            "Performs relatively few swaps.",
        ],
        "disadvantages": [
            "Always performs O(n²) comparisons.",
            "Slow for large datasets.",
            "Not stable in the general case.",
        ],
        "best_use_case": "Small datasets where minimizing swaps is important.",
    },

    "insertion_sort": {
        "name": "Insertion Sort",
        "category": "Sorting",
        "description": (
            "Builds the sorted portion of the list one element at a time "
            "by inserting each element into its correct position."
        ),
        "time_complexity": {
            "best": "O(n)",
            "average": "O(n²)",
            "worst": "O(n²)",
        },
        "space_complexity": "O(n)",
        "stable": True,
        "requires_sorted": False,
        "advantages": [
            "Efficient for small or nearly sorted datasets.",
            "Stable sorting algorithm.",
            "Simple implementation.",
        ],
        "disadvantages": [
            "Slow for large unsorted datasets.",
            "Requires many shifts in the worst case.",
        ],
        "best_use_case": "Small or nearly sorted datasets.",
    },

    "merge_sort": {
        "name": "Merge Sort",
        "category": "Sorting",
        "description": (
            "Divides the list into smaller sections, recursively sorts "
            "them, and merges the sorted sections."
        ),
        "time_complexity": {
            "best": "O(n log n)",
            "average": "O(n log n)",
            "worst": "O(n log n)",
        },
        "space_complexity": "O(n)",
        "stable": True,
        "requires_sorted": False,
        "advantages": [
            "Consistent O(n log n) performance.",
            "Stable sorting algorithm.",
            "Works well with large datasets.",
        ],
        "disadvantages": [
            "Requires additional memory.",
            "More complex than simple quadratic sorting algorithms.",
        ],
        "best_use_case": "Large datasets where predictable performance and stability are important.",
    },

    "quick_sort": {
        "name": "Quick Sort",
        "category": "Sorting",
        "description": (
            "Selects a pivot, partitions the list around the pivot, "
            "and recursively sorts the resulting sections."
        ),
        "time_complexity": {
            "best": "O(n log n)",
            "average": "O(n log n)",
            "worst": "O(n²)",
        },
        "space_complexity": "O(n)",
        "stable": False,
        "requires_sorted": False,
        "advantages": [
            "Fast average-case performance.",
            "Good cache performance.",
            "Widely used in practice.",
        ],
        "disadvantages": [
            "Can degrade to O(n²) with poor pivot selection.",
            "Not stable.",
        ],
        "best_use_case": "General-purpose sorting when average-case performance is important.",
    },

    "heap_sort": {
        "name": "Heap Sort",
        "category": "Sorting",
        "description": (
            "Builds a heap from the elements and repeatedly extracts "
            "the largest element to produce a sorted list."
        ),
        "time_complexity": {
            "best": "O(n log n)",
            "average": "O(n log n)",
            "worst": "O(n log n)",
        },
        "space_complexity": "O(n)",
        "stable": False,
        "requires_sorted": False,
        "advantages": [
            "Guaranteed O(n log n) time.",
            "Provides predictable worst-case performance.",
        ],
        "disadvantages": [
            "Not stable.",
            "Generally slower in practice than optimized quick sort.",
        ],
        "best_use_case": "When guaranteed O(n log n) performance is required.",
    },

    "counting_sort": {
        "name": "Counting Sort",
        "category": "Sorting",
        "description": (
            "Counts the frequency of each integer value and uses those "
            "counts to construct the sorted result."
        ),
        "time_complexity": {
            "best": "O(n + k)",
            "average": "O(n + k)",
            "worst": "O(n + k)",
        },
        "space_complexity": "O(n + k)",
        "stable": True,
        "requires_sorted": False,
        "advantages": [
            "Can be faster than comparison-based sorting.",
            "Linear-time performance when the value range is small.",
        ],
        "disadvantages": [
            "Only supports non-negative integers in the current implementation.",
            "Can use large amounts of memory when the value range is large.",
        ],
        "best_use_case": "Integer data with a relatively small value range.",
    },

    "radix_sort": {
        "name": "Radix Sort",
        "category": "Sorting",
        "description": (
            "Sorts integers digit by digit, processing each digit from "
            "the least significant to the most significant."
        ),
        "time_complexity": {
            "best": "O(d(n + k))",
            "average": "O(d(n + k))",
            "worst": "O(d(n + k))",
        },
        "space_complexity": "O(n + k)",
        "stable": True,
        "requires_sorted": False,
        "advantages": [
            "Can achieve near-linear performance for integers.",
            "Does not compare elements directly.",
        ],
        "disadvantages": [
            "Current implementation supports only non-negative integers.",
            "Performance depends on the number of digits.",
            "Requires additional memory.",
        ],
        "best_use_case": "Large collections of non-negative integers with a manageable number of digits.",
    },

    "bucket_sort": {
        "name": "Bucket Sort",
        "category": "Sorting",
        "description": (
            "Distributes integer values into buckets based on their "
            "value and combines the buckets in order."
        ),
        "time_complexity": {
            "best": "O(n + k)",
            "average": "O(n + k)",
            "worst": "O(n + k)",
        },
        "space_complexity": "O(n + k)",
        "stable": True,
        "requires_sorted": False,
        "advantages": [
            "Can be efficient when the value range is manageable.",
            "Supports negative integers in the current implementation.",
            "Simple implementation for integer data.",
        ],
        "disadvantages": [
            "Memory usage depends on the range of values.",
            "A very large value range can require excessive memory.",
            "The current implementation is specialized for integer values.",
        ],
        "best_use_case": "Integer data with a manageable range of values.",
    },
}


def get_info(name: str) -> dict:
    """
    Returns information about the requested algorithm.

    Args:
        name: Name of the algorithm.

    Returns:
        A dictionary containing the algorithm's information.

    Raises:
        ValueError: If the algorithm name is not found.
    """
    name = name.lower()

    if name not in _ALGORITHM_INFO:
        raise ValueError(
            f"Unknown algorithm: {name}. "
            f"Use list_algorithms() to see available algorithms."
        )

    return _ALGORITHM_INFO[name]


def show_info(name: str) -> None:
    """
    Prints information about the requested algorithm.

    Args:
        name: Name of the algorithm.

    Raises:
        ValueError: If the algorithm name is not found.
    """
    info = get_info(name)

    print(f"Algorithm: {info['name']}")
    print(f"Category: {info['category']}")
    print(f"\nDescription:\n{info['description']}")

    print("\nTime Complexity:")
    print(f"  Best:    {info['time_complexity']['best']}")
    print(f"  Average: {info['time_complexity']['average']}")
    print(f"  Worst:   {info['time_complexity']['worst']}")

    print(f"\nSpace Complexity: {info['space_complexity']}")
    print(f"Stable: {info['stable']}")
    print(f"Requires Sorted Data: {info['requires_sorted']}")

    print("\nAdvantages:")
    for advantage in info["advantages"]:
        print(f"  - {advantage}")

    print("\nDisadvantages:")
    for disadvantage in info["disadvantages"]:
        print(f"  - {disadvantage}")

    print(f"\nBest Use Case:\n{info['best_use_case']}")


def list_algorithms() -> list[str]:
    """
    Returns a list of all available algorithms.

    Returns:
        A list containing the names of all available algorithms.
    """
    return list(_ALGORITHM_INFO.keys())