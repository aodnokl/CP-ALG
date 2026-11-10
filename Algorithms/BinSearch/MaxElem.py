# ==========================================
# PROBLEM: Maximum in a Growing and Decreasing Vector (DyV / Binary Search)
# ==========================================
# Description:
# Let v be an array of integers, of length greater than 0, containing a sequence 
# of strictly increasing values up to a certain index k and strictly decreasing 
# from k to the end. Design a Divide and Conquer (DyV) function to find 
# this index k with the best possible complexity O(log n) and constant space O(1)[cite: 1].
#
# Example:
# v = [3, 7, 12, 30, 25, 19, 14, 9, 4, 2] -> k = 3 (value 30)[cite: 1]
#
# Core Properties of Binary Search for this Problem:
# Mastering this variant involves analyzing the slope by checking the neighbors of the middle element:
# 1. Local Monotonicity Property: Index k represents the peak of the array, 
#    where the value is greater than its adjacent elements.
# 2. If v[middle] < v[middle + 1]: We are on the upward slope. The peak must be 
#    to the right, so discard the left half (left = middle + 1).
# 3. If v[middle] > v[middle + 1]: We are on the downward slope or at the peak. 
#    The peak is at middle or to the left, so discard the right half (right = middle).



from typing import List
def max_elem(array: List[int]):
    left, right = 0, len(array)

    while left <= right:
        middle = (left + right) // 2

        if array[middle] > array[middle + 1]:
            right = middle

        elif array[middle] < array[middle + 1]:
            left = middle + 1


    return left