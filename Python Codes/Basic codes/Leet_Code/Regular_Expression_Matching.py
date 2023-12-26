import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.fullmatch(re.compile(p), s)
        if match:
            return True
        else:
            return False

print(Solution().isMatch('aa', 'a*'))


