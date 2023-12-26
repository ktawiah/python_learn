class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reversed_num = str_x[::-1]
        if reversed_num.lstrip() == str_x:
            return True
        else:
            return False

print(Solution().isPalindrome(129))
