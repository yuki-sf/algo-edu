import math

def linear_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in an array using linear search.

    Args:
        arr: A list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        O(n)

    Space Complexity:
        O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

def binary_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted array using binary search.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def jump_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted array using jump search.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        O(sqrt(n))

    Space Complexity:
        O(1)
    """
    n = len(arr)
    if n == 0:
        return -1

    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    return -1

def interpolation_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted, uniformly distributed array
    using interpolation search.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        Average: O(log(log n))
        Worst: O(n)

    Space Complexity:
        O(1)
    """
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            return low if arr[low] == target else -1
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def exponential_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted array using exponential search.

    The algorithm first finds a suitable search range by repeatedly
    doubling the index, then performs binary search within that range.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    bound = 1
    while bound < n and arr [bound] >= target:
        bound *= 2
    left = bound // 2
    right = min(bound, n-1)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def ternary_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted array using ternary search.

    The search space is divided into three parts at each iteration.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
    return -1

def fibonacci_search(arr: list[int], target: int) -> int:
    """
    Search for a target value in a sorted array using Fibonacci search.

    The algorithm uses Fibonacci numbers to divide the search space
    instead of using the midpoint directly.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1

    while fib > 1:
        i = min(offset + fib2, n-1)
        if arr[i] == target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2  = fib - fib1
        else:
            return i

    if fib and offset != -1:
        return offset + 1
    return -1

def first_occurrence(arr: list[int], target: int) -> int:
    """
    Find the first occurrence of a target in a sorted array.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the first occurrence if found, otherwise -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def last_occurrence(arr: list[int], target: int) -> int:
    """
    Find the last occurrence of a target in a sorted array.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        The index of the last occurrence if found, otherwise -1.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

def search_range(arr: list[int], target: int) -> tuple[int, int]:
    """
    Find the first and last occurrence of a target in a sorted array.

    Args:
        arr: A sorted list of integers.
        target: The value to search for.

    Returns:
        A tuple containing (first_index, last_index).
        Returns (-1, -1) if the target is not found.

    Time Complexity:
        O(log n)

    Space Complexity:
        O(1)
    """
    return (
        first_occurrence(arr, target),
        last_occurrence(arr, target),
    )