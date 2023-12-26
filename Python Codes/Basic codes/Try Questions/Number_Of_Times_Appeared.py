class Times_Appeared:
    def __init__(self, num: int, target_num: int):
        self.num = num
        self.target_num = target_num

    def timesAppeared(self):
        count = 0
        for digit in str(self.num):
            if digit == str(self.target_num):
                count += 1
            else:
                count += 0

        print(f'{self.target_num} appeared {count} times in {self.num}')

Times_Appeared(998795, 9).timesAppeared()