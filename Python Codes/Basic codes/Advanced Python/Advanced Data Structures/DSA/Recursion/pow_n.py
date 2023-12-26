class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = 0
        def_x = x
        return self.power_n(x, n, count, def_x)

    def power_n(
        self, x: float, n: float, count: float, def_x: float, cache={}
    ) -> float:
        print(n, x)
        if n in cache:
            return cache[n]
        if n > 0 and count == n - 1:
            cache[n] = x
            return x
        if n < 0 and count == -n + 1:
            cache[n] = x
            return x

        count += 1
        x = 1 / (x * def_x) if n < 0 else x * def_x
        value = self.power_n(x, n, count, def_x)
        cache[n] = value
        return value


print(Solution().myPow(8.88023, 1000))
