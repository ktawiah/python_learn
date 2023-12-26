class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person_number = 1
        direction = 1  # 1 for forward, -1 for backward

        for second in range(time):
            if person_number == n:
                direction = -1
            elif person_number == 1:
                direction = 1

            person_number += direction

        return person_number

print(Solution().passThePillow(4, 5))

