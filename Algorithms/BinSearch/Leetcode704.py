# ==========================================
# PROBLEM: Binary Search (LeetCode 704)
# ==========================================
# Description:
# Given an array of integers nums sorted in ascending order, and an integer 
# target, write a function to search for target in nums. If target exists, 
# return its index. Otherwise, return -1.
# You must implement a solution with a logarithmic runtime complexity O(log n) 
# and use only constant extra space O(1).
#
# Core Properties of Binary Search for this Problem:
# Mastering this variant means understanding the search space reduction and how to discard halves:
# 1. Sorted Monotonicity Property: Since the array is sorted in ascending order, 
#    we can compare the middle element directly with the target to eliminate half of the remaining search space.
# 2. If nums[middle] == target: We have found the target and can return its index directly.
# 3. If nums[middle] > target: All elements to the right of middle are greater than target 
#    because the array is sorted. Discard the right half (right = middle - 1).
# 4. If nums[middle] < target: All elements to the left of middle are smaller than target. 
#    Discard the left half (left = middle + 1).


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # The iterative approach
        while left <= right:
            middle = (left + right) // 2

            # Index points on the target
            if nums[middle] ==  target:
                return middle

            # If it is less than the target we should not look it up on the left part
            elif nums[middle] < target:
                left = middle + 1
                
            # The same as left but now with the right part
            else:
                right = middle - 1

        return -1