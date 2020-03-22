import time
from typing import Callable

import numpy as np


NUM_ELEMENTS = 6

# Auxiliary functions
def do_sort(
    sorting_func: Callable[[np.ndarray], np.ndarray],
    func_name: str,
    arr: np.ndarray
):
    arr_copy = arr.copy()
    print("Sorting", NUM_ELEMENTS, "random elements with", func_name, "...")
    start_time = time.time()
    arr_copy = sorting_func(arr_copy)
    if not is_non_decreasing_array(arr_copy):
        print("Erro, algoritmo não funcionou!")
    total_time = time.time() - start_time
    print("Seconds taken:", total_time)
    print("")

def is_non_increasing_array(arr: np.ndarray) -> bool:
    """Returns if the array is non-increasing"""
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            return False
    return True

def is_non_decreasing_array(arr: np.ndarray) -> bool:
    """Returns if the array is non-decreasing"""
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False
    return True

# Sorting algorithms
def random_guess_sort(arr: np.ndarray) -> np.ndarray:
    """
    Sorts by trying to guess which position each element goes to.
    Guesses are random and can be repeated.
    """
    success = False
    new_arr = np.empty(len(arr), dtype=arr.dtype)
    pos_guess_arr = np.empty(len(arr), dtype=int)
    while True:
        # For each element in the array
        # Choose a random position that it goes to
        for i, element in enumerate(arr):
            pos_guess_arr[i] = np.random.randint(0, len(arr))

        # Check if the guesses are valid
        valid_guess = True
        for i, guess in enumerate(pos_guess_arr):
            # Check if the guesses occur more than once
            if len(pos_guess_arr[pos_guess_arr == guess]) > 1:
                valid_guess = False
                break

        if valid_guess:
            # Copy value to new array
            for i, guess in enumerate(pos_guess_arr):
                new_arr[guess] = arr[i]
            #  Check if it's in the right order
            if is_non_decreasing_array(new_arr):
                return new_arr

def bogo_sort(arr: np.ndarray) -> np.ndarray:
    """Shuffle elements until they are in order"""
    while not is_non_decreasing_array(arr):
        np.random.shuffle(arr)
    return arr

def slow_sort(arr: np.ndarray) -> np.ndarray:
    def slow_sort_recursive(arr, i, j):
        if i >= j:
            return
        m = (i + j) // 2
        slow_sort_recursive(arr, i, m)
        slow_sort_recursive(arr, m+1, j)
        if arr[j] < arr[m]:
            swap = arr[j]
            arr[j] = arr[m]
            arr[m] = swap
        slow_sort_recursive(arr, i, j-1)
    slow_sort_recursive(arr, 0, len(arr)-1)
    return arr

def random_swap_sort(arr: np.ndarray) -> np.ndarray:
    """Swap 2 elements at random until it's ordered"""
    while not is_non_decreasing_array(arr):
        idx1 = np.random.randint(len(arr))
        idx2 = np.random.randint(len(arr))

        swap = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = swap
    return arr

def random_pancake_sort(arr: np.ndarray) -> np.ndarray:
    """Randomly reverse the order of [0, rand_n] until it's sorted"""
    while not is_non_decreasing_array(arr):
        flip_idx = np.random.randint(len(arr)+1)
        arr[:flip_idx] = np.flip(arr[:flip_idx])
    return arr


if __name__ == "__main__":
    arr = np.random.rand(NUM_ELEMENTS)

    do_sort(random_guess_sort, "Random Guess Sort", arr)
    do_sort(random_pancake_sort, "Random Pancake Sort", arr)
    do_sort(bogo_sort, "Bogo Sort", arr)
    do_sort(random_swap_sort, "Random Swap Sort", arr)
    do_sort(slow_sort, "Slow Sort", arr)