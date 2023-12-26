from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for level in range(len(nums) - 1):
        for index in range(level + 1, -1):
            if nums[index] < nums[index - 1]:
                temp = nums[index]
                nums[index] = nums[index - 1]
                nums[index - 1] = temp
    return nums


def bubble_sort(nums: List[int]) -> List[int]:
    for level in range(len(nums)):
        for index in range(1, len(nums) - level):
            if nums[index - 1] > nums[index]:
                temp = nums[index]
                nums[index] = nums[index - 1]
                nums[index - 1] = temp
    return nums


def selection_sort(nums: List[int]):
    for level in range(len(nums)):
        min_val = float("inf")
        for comp in range(level, len(nums)):
            if nums[comp] < min_val:
                min_val = nums[comp]
                min_idx = comp
        temp = nums[min_idx]
        nums[min_idx] = nums[level]
        nums[level] = temp

    return nums


print(insertion_sort([6, 3, 1, 7, 9]))
