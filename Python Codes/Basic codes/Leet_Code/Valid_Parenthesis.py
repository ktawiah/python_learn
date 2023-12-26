class Solution:
    def isValid(self, s: str) -> bool:
        str_opening = ['{', '(', '[']
        str_closing = ['}', ')', ']']
        str_me = 5

        for opening, closing in zip(str_opening, str_closing):
            while f'{opening}{closing}' in s:
                return True
            return False


print(Solution().isValid("(]"))