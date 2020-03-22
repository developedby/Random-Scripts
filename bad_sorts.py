import time
from typing import Callable

import numpy as np


NUM_ELEMENTS = 6

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

def random_guess_sort(arr: np.ndarray) -> np.ndarray:
    """
    Sorts by trying to guess which position each element goes to.
    Guesses are random and can be repeated.
    """
    success = False
    while True:
        # For each element in the array
        # Choose a random position that it goes to
        pos_guess_arr = np.empty(len(arr), dtype=int)
        for i, element in enumerate(arr):
            pos_guess_arr[i] = np.random.randint(0, len(arr))

        # Try to place the elements in the new order
        new_arr = np.empty(len(arr), dtype=arr.dtype)
        valid_guess = True
        for i, guess in enumerate(pos_guess_arr):
            # Check if the guess occurs more than once
            if len(pos_guess_arr[pos_guess_arr == guess]) > 1:
                valid_guess = False
            # Copy value to new array
            new_arr[guess] = arr[i]

        # If it succeeds check if it's in the right order
        if valid_guess:
            # If is in order
            if is_non_decreasing_array(new_arr):
                return new_arr

def bogo_sort(arr: np.ndarray) -> np.ndarray:
    while not is_non_decreasing_array(arr):
        np.random.shuffle(arr)
    return arr

def do_sort(
    sorting_func: Callable[[np.ndarray], np.ndarray],
    func_name: str,
    arr: np.ndarray
):
    arr_copy = arr.copy()
    print("Sorting", NUM_ELEMENTS, "random elements with", func_name, "...")
    start_time = time.time()
    random_guess_sort(arr_copy)
    total_time = time.time() - start_time
    print("Seconds taken:", total_time)
    print("")


if __name__ == "__main__":
    arr = np.random.rand(NUM_ELEMENTS)

    do_sort(random_guess_sort, "Random Guess Sort", arr)
    do_sort(bogo_sort, "Bogo Sort", arr)
