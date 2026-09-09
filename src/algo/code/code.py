import inspect

from algo.search import (
    linear_search,
    binary_search,
    jump_search,
    interpolation_search,
    exponential_search,
    ternary_search,
    fibonacci_search,
    first_occurrence,
    last_occurrence,
    search_range,
)

from algo.sort import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
)


_ALGORITHMS = {
    "linear_search": linear_search,
    "binary_search": binary_search,
    "jump_search": jump_search,
    "interpolation_search": interpolation_search,
    "exponential_search": exponential_search,
    "ternary_search": ternary_search,
    "fibonacci_search": fibonacci_search,
    "first_occurrence": first_occurrence,
    "last_occurrence": last_occurrence,
    "search_range": search_range,

    "bubble_sort": bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": merge_sort,
    "quick_sort": quick_sort,
    "heap_sort": heap_sort,
    "counting_sort": counting_sort,
    "radix_sort": radix_sort,
    "bucket_sort": bucket_sort,
}


def get_code(name: str) -> str:
    """
    Returns the source code of the requested algorithm.

    Args:
        name: Name of the algorithm.

    Returns:
        The source code of the algorithm as a string.

    Raises:
        ValueError: If the algorithm name is not found.
    """
    name = name.lower()

    if name not in _ALGORITHMS:
        raise ValueError(
            f"Unknown algorithm: {name}. "
            f"Use list_algorithms() to see available algorithms."
        )

    return inspect.getsource(_ALGORITHMS[name])


def show_code(name: str) -> None:
    """
    Prints the source code of the requested algorithm.

    Args:
        name: Name of the algorithm.

    Raises:
        ValueError: If the algorithm name is not found.
    """
    print(get_code(name))


def list_algorithms() -> list[str]:
    """
    Returns a list of all available algorithms.

    Returns:
        A list containing the names of all available algorithms.
    """
    return list(_ALGORITHMS.keys())