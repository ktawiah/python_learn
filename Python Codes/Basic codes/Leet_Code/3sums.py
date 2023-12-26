from typing import List
from itertools import combinations as com


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_list = set(com(nums, 3))
        new_list = set()
        for i, j, k in nums_list:
            if i + k + j == 0:
                new_list.add((i, j, k))
        return new_list


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
