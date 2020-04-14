from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ones = 0

        for x in nums:
            if x == 1:
                count += 1
            if x == 0:
                max_ones = max(max_ones, count)
                count = 0

        return max(max_ones, count)