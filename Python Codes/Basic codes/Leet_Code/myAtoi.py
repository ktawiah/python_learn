import re


class Solution:
    def myAtoi(self, s: str) -> int:
        regex = r"^(-|\+)?\d+"
        match = re.search(regex, s.lstrip())
        if match:
            if -(2**31) <= int(match.group()) <= (2**31) - 1:
                return int(match.group())
            elif int(match.group()) < -(2**31):
                return -(2**31)
            else:
                return (2**31) - 1
        else:
            return 0


print(Solution().myAtoi("-91283472332"))
