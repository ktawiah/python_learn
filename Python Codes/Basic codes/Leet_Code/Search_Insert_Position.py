from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if max(nums) >= target >= min(nums):
                if target == nums[i]:
                    return i
                elif nums[i] < target < nums[i + 1]:
                    return i + 1
            elif target < min(nums):
                return 0
            else:
                return len(nums)


print(Solution().searchInsert([1, 3, 6], 0))


