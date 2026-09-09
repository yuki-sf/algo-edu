def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using bubble sort.

    Args:
        arr: A list of integers.

    Returns:
        A new sorted list of integers.

    Time Complexity:
        Best: O(n)
        Average: O(n²)
        Worst: O(n²)

    Space Complexity:
        O(n)
    """
    result = arr.copy()

    n = len(result)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result

def selection_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using selection sort.

    Args:
        arr: A list of integers.

    Returns:
        A new sorted list of integers.

    Time Complexity:
        Best: O(n²)
        Average: O(n²)
        Worst: O(n²)

    Space Complexity:
        O(n)
    """
    result = arr.copy()

    n = len(result)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j

        result[i], result[min_index] = result[min_index], result[i]

    return result

def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using insertion sort.

    Args:
        arr: A list of integers.

    Returns:
        A new sorted list of integers.

    Time Complexity:
        Best: O(n)
        Average: O(n²)
        Worst: O(n²)

    Space Complexity:
        O(n)
    """
    result = arr.copy()

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result

def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using merge sort.

    Args:
        arr: A list of integers.

    Returns:
        A new sorted list of integers.

    Time Complexity:
        Best: O(n log n)
        Average: O(n log n)
        Worst: O(n log n)

    Space Complexity:
        O(n)
    """
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def quick_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Quick Sort algorithm.

    The input list is not modified; a sorted copy is returned.

    Args:
        arr: A list of integers to sort.

    Returns:
        A new list containing the elements in ascending order.

    Complexity:
        Best/Average Time: O(n log n)
        Worst Time: O(n²)
        Space: O(n) including the copied list
    """
    result = arr.copy()

    def partition(low: int, high: int) -> int:
        pivot = result[high]
        i = low - 1

        for j in range(low, high):
            if result[j] <= pivot:
                i += 1
                result[i], result[j] = result[j], result[i]

        result[i + 1], result[high] = result[high], result[i + 1]
        return i + 1

    def quicksort(low: int, high: int) -> None:
        if low < high:
            pivot_index = partition(low, high)

            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    quicksort(0, len(result) - 1)

    return result

def heap_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using heap sort.

    Args:
        arr: A list of integers.

    Returns:
        A new sorted list of integers.

    Time Complexity:
        Best: O(n log n)
        Average: O(n log n)
        Worst: O(n log n)

    Space Complexity:
        O(n)
    """
    result = arr.copy()
    n = len(result)

    def heapify(size: int, root: int) -> None:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and result[left] > result[largest]:
            largest = left

        if right < size and result[right] > result[largest]:
            largest = right

        if largest != root:
            result[root], result[largest] = result[largest], result[root]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(i, 0)

    return result

def counting_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using counting sort.

    This implementation supports non-negative integers.

    Args:
        arr: A list of non-negative integers.

    Returns:
        A new sorted list of integers.

    Raises:
        ValueError: If the array contains a negative integer.

    Time Complexity:
        O(n + k), where k is the range of values.

    Space Complexity:
        O(n + k)
    """
    if not arr:
        return []

    if min(arr) < 0:
        raise ValueError("counting_sort only supports non-negative integers")

    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    result = []

    for num, frequency in enumerate(count):
        result.extend([num] * frequency)

    return result

def radix_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of non-negative integers using radix sort.

    Args:
        arr: A list of non-negative integers.

    Returns:
        A new sorted list of integers.

    Raises:
        ValueError: If the array contains a negative integer.

    Time Complexity:
        O(d * (n + k)), where d is the number of digits
        and k is the base (10).

    Space Complexity:
        O(n + k)
    """
    if not arr:
        return []

    if min(arr) < 0:
        raise ValueError("radix_sort only supports non-negative integers")

    result = arr.copy()
    max_value = max(result)
    place = 1

    while max_value // place > 0:
        buckets = [[] for _ in range(10)]

        for num in result:
            digit = (num // place) % 10
            buckets[digit].append(num)

        result = [
            num
            for bucket in buckets
            for num in bucket
        ]

        place *= 10

    return result

def bucket_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers using bucket sort.

    Args:
        arr: A list of integers.

    Returns:
        A new sorted list of integers.

    Time Complexity:
        Average: O(n + k)
        Worst: O(n²)

        where k is the number of buckets.

    Space Complexity:
        O(n + k)
    """
    if not arr:
        return []

    min_value = min(arr)
    max_value = max(arr)

    bucket_count = max_value - min_value + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        buckets[num - min_value].append(num)

    return [
        num
        for bucket in buckets
        for num in bucket
    ]

