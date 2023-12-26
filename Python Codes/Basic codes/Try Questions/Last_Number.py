#Question 4

from typing import List

class Last_Occurrence:
    def __init__(self, arr: List[int], target_num: int):
        self.arr = arr
        self.target = target_num

    def findPosition(self):
        for element in self.arr:
            if self.target == element:
                last_position = self.arr.index(element) + 1

        return last_position

my_Object = Last_Occurrence([2, 4, 2, 5, 6, 8, 2, 6, 3, 4, 5, 6, 3, 2, 2, 7, 8, 9, 1, 2, 2, 1], 1)
print(my_Object.findPosition())