# ==========================================
# PROBLEM: 136. Single Number (Easy)
# ==========================================
# Description:
# Given a non-empty array of integers nums, every element appears twice 
# except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use 
# only constant extra space.
#
# Core Properties of XOR for Competitive Programming:
# Mastering XOR means mastering its algebraic properties:
# 1. Identity Property (x ^ 0 = x): Xoring a number with 0 leaves it unchanged.
# 2. Self-Inverse Property (x ^ x = 0): Xoring a number with itself cancels it out completely. 
#    This is the most used property in CP (e.g., finding duplicates or pairs).
# 3. Commutative (a ^ b = b ^ a): Order does not matter.
# 4. Associative ((a ^ b) ^ c = a ^ (b ^ c)): Grouping does not matter.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # The result will be this
        single_value = 0

        # XOR all numbers together using the properties above.
        # Numbers that appear twice will cancel out (x ^ x = 0).
        # Only the unique number will remain (0 ^ single = single).
        for elem in nums:
            single_value ^= elem

        return single_value
