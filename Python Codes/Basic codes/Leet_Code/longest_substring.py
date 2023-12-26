import re
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if re.fullmatch(r'^[a-zA-Z]$', s):
            substring = []
            for char in range(len(s)):
                for i in range(len(s)):
                    substring.append(s[char:i])
            print(substring)
            no_repeats_string = []
            for string in substring:
                if len(string) == len(set(string)):
                    no_repeats_string.append(string)
                else:
                    continue
            no_repeats_string.sort(key=len)
            return len(no_repeats_string[-1])
        else:
            return len(s)


print(Solution().lengthOfLongestSubstring("abcabcbb"))
