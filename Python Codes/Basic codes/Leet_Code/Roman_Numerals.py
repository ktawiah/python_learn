class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s_pieces = list(s)
        sum = 0
        prev_value = 0
        for i in range(len(s_pieces)):
            value = roman_numerals[s_pieces[i]]
            if value > prev_value:
                sum -= prev_value
                sum += value - prev_value
            else:
                sum += value
            prev_value = value
        return sum



print(Solution().romanToInt("VI"))
