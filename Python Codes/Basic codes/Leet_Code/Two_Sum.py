from itertools import combinations
from typing import List, Any


class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[Any] | str:
        for i, j in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]
        return f"Sum of nums for {target} not found in list"


print(Solution().twoSum([2, 7, 11, 15], 17))