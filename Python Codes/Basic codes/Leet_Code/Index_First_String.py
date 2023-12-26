# Question 28
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for element in haystack:
        #     if needle in haystack and element == needle[0]:
        #         return haystack.index(element)
        # return -1

        return next(
            (
                haystack.index(element)
                for element in haystack
                if needle in haystack and element == needle[0]
            ),
            -1,
        )


print(Solution().strStr("mississippi", "issip"))
