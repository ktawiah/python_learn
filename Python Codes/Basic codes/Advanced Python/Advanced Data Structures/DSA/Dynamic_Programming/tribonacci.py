from typing import List, Union


def search_ascending(nums: List[int], target: int) -> Union[int, str]:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        right = mid
    return left if nums[left] == target else -1


def search_descending(nums: List[int], target: int) -> Union[int, str]:
    left, right = 0, len(nums) - 1
    while left > right:
        mid = (left + right) // 2
        if nums[mid] < target:
            right = mid - 1
        left = mid
    return right - 1


# print(search_ascending([1, 2, 2, 4, 5], 2))
print(search_descending([5, 4, 3, 2, 2, 1], 2))
