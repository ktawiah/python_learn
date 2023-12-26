from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # full_list = []        #
        # for value in range(1, arr[-1]+1):
        #     full_list.append(value)
        #
        #
        # for value in full_list:
        #     if value not in arr:
        #         new_list.append(value)\

        # if len(new_list) < k:
        #     return arr[-1] + k - len(new_list)
        # else:
        #     return new_list[k-1]

        full_list = [value for value in range(1, arr[-1] + 1)]
        new_list = [value for value in full_list if value not in arr]
        return arr[-1] + k - len(new_list) if len(new_list) < k else new_list[k - 1]


print(Solution().findKthPositive([1, 2, 3, 4], 2))
