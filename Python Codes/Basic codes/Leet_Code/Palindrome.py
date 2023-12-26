class Palindrome:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reversed_num = ''
        for i in range(len(str_x), 0, -1):
            reversed_num += str_x[i - 1]

        if reversed_num.lstrip() == str_x:
            return True
        else:
            return False


print(Palindrome().isPalindrome(121))
