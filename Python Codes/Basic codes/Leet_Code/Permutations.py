from typing import List
from itertools import permutations


class Solution:
    def permutation(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        return list(perm)


print(Solution().permutation([1,2,3]))