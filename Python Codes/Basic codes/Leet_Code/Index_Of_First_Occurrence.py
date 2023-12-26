class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle[0])
        else:
            return -1

        return next((haystack.index(needle[0]) for _ in [0] if needle in haystack), -1)


print(Solution().strStr("sadbutsad", "sad"))
