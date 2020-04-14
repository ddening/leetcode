from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()                    # create empty hashmap

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in hashMap:
                return [hashMap[diff], idx]

            hashMap[nums[idx]] = idx        # add new key-pair [value, index]

# create empty hashmap
# equation: target = value_1 + value_2 (index of value_1 != index of value_2)
# => target - value_1 = value_2
# hold value_1 := idx
# look up if value_2 := diff exists in hashmap
# add value_2 to our look-up-table as a key-pair of [value, index_in_array]
