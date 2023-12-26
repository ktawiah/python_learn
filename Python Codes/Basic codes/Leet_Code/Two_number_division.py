class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor > 0 and dividend >= 0:
            quotient = dividend // divisor
        elif divisor < 0 <= dividend:
            quotient = -(dividend // -divisor)
        elif divisor < 0 >= dividend:
            quotient = -dividend // -divisor
        else:
            quotient = -(-dividend // divisor)

        if (-2)**31 <= quotient <= (2**31) - 1:
            return quotient
        elif quotient > (2**31) - 1:
            return (2**31) - 1
        else:
            return (-2)**31

print(Solution().divide(-2147483648,-3))