import unittest
from typing import List
from itertools import combinations


class Solution:
    def maxArea(self, height: List[int]) -> int:
        for i, j in combinations(height, 2):
            return min(height[i], height[j])


class TestSolution(unittest.TestCase):
    def test_maxArea(self):
        s = Solution()
        self.assertEqual(s.maxArea([4, 3, 2, 1, 4]), 16)
        self.assertEqual(s.maxArea([1, 2, 1]), 2)
        self.assertEqual(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)


if __name__ == "__main__":
    print(Solution().maxArea([4, 3, 2, 1, 4]))
    unittest.main()
