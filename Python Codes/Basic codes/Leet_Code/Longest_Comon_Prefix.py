from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for str_elements in strs:
            for i in str_elements:
                i