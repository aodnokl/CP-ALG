# ==========================================
# PROBLEM: Search Insert Position (Binary Search)
# ==========================================
# Description:
#
# Given a sorted array of distinct integers and a target value, return the 
# index if the target is found. If not, return the index where it would be 
# if it were inserted in order. 
# You must write an algorithm with O(log n) runtime complexity and O(1) space.
#
#
# Core Properties of Binary Search for this Problem:
# Mastering this variant involves finding lower/upper bounds and handling insertion points:
# 1. Sorted Monotonicity Property: Since the array is strictly increasing and sorted, 
#    we can use binary search to narrow down the exact position in logarithmic time.
# 2. If nums[middle] == target: The target is found at index middle, so return middle.
# 3. If nums[middle] < target: The target must belong to the right half. Move the 
#    left boundary up (left = middle + 1).
# 4. If nums[middle] > target: The target must belong to the left half. Move the 
#    right boundary down (right = middle - 1).
# 5. Insertion Index: When the loop terminates without finding the target, the 
#    `left` pointer naturally points to the exact index where the target should be inserted.

from typing import List
def insert_position(array: List[int], target: int) -> int:

    left, right = 0, len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        
        elif array[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return left