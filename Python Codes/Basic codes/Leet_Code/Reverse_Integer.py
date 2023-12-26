class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reverse_str = int(str(x)[::-1])
        else:
            x *= -1
            reverse_str = -1 * int(str(x)[::-1])

        if -(2**31) <= reverse_str <= 2**31:
            return reverse_str
        else:
            return 0


print(Solution().reverse(-120))
