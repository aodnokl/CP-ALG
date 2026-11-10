# ==========================================
# PROBLEM: Elemento igual a su índice (Binary Search)
# ==========================================
# Description:
# Given a sorted list/vector v of integers in increasing order with no 
# repeated elements, find if there is any index i such that v[i] == i 
# (its value matches its index). Return that index/value, or None if 
# no such element exists.
# You must implement a solution with a logarithmic runtime complexity O(log n) 
# and use only constant extra space O(1).
#
# Core Properties of Binary Search for this Problem:
# Mastering this variant means understanding monotonicity and how to discard halves:
# 1. Strict Monotonicity Property: Since the array is strictly increasing without 
#    duplicates, v[i] grows at least by 1 per index. This guarantees that at 
#    most one such index can exist in the entire array.
# 2. If v[middle] > middle: All elements to the right will also satisfy v[i] > i 
#    because values grow faster or equal to indices. Discard the right half (right = middle - 1).
# 3. If v[middle] < middle: All elements to the left will satisfy v[i] < i. 
#    Discard the left half (left = middle + 1).
# 4. If v[middle] == middle: We have found the unique matching element and can 
#    return it directly (or store it and narrow down if looking for specific bounds).

from typing import List, Tuple


def same_index(data: List[int]) -> Tuple:
    left, right = 0, len(data) - 1
    while left <= right:
        middle = (left + right) // 2  # Gettign the middle of the list

        if data[middle] == middle:  # The base case if the index is the value
            return (data[middle], middle)

        elif data[middle] < middle:
            left = middle + 1   # Not searching in the left part

        else:
            right = middle - 1 # Not searching in the right part

    return None


# The solution is O(log n) because it is the Binary search
# Space complexity is O(1)