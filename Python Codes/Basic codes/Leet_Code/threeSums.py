from itertools import combinations as com
from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums_list = com(nums, 3)
#         new_list = [sorted([i, j, k]) for i, j, k in nums_list if i + k + j == 0]
#         app_list = []
#         for num in new_list:
#             if num not in app_list:
#                 app_list.append(num)
#         return app_list

#     print({1, 1, 2})


class Solution:
    def maxArea(self, height: List[int]) -> int:
        sort_nums = sorted(height)
        print(sort_nums)
        pointer_one, pointer_two = 0, len(sort_nums) - 1
        while pointer_one < pointer_two:
            if (
                sort_nums[pointer_two] == sort_nums[pointer_two - 1]
                and len(sort_nums) > 2
            ):
                pointer_two -= 1
            else:
                return sort_nums[pointer_two - 1] ** 2


print(Solution().maxArea([4, 3, 2, 1, 4]))
