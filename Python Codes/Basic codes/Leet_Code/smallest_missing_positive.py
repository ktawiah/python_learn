from typing import List 
class Solution:
    def missingPositive(self, nums: List[int]) -> int:
        for i in nums:
            return min(nums)
        return max(nums) + 1

print(Solution().missingPositive([1,2,0]))