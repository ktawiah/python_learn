from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = sorted(set(nums))
        for i, element in zip(range(0, len(num_set)), num_set):
            nums[i] = element
        count = 0
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                break
        return count + 1


print(Solution().removeDuplicates([-1,0,0,0,0,3,3]))