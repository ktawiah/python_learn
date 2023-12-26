from typing import List


def search(nums: List[int], target: int) -> int:
    """Return the position of the first occurrence of a given number in list

    Parameters
    ----------
    nums : List[int]
        List of integer value to search through
    target : int
        Value to find position in nums

    Returns
    -------
    int
        Position of target value
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    return [
        search_first(nums, target, left, right),
        search_second(nums, target, left, right),
    ]


def search_first(nums_list, target, left, right, cache={}):
    if left > right:
        return -1

    midpoint = (left + right) // 2

    if left == right and nums_list[midpoint] != target:
        return -1

    if midpoint in cache:
        return cache[midpoint]

    if nums_list[midpoint] == target:
        if nums_list[midpoint - 1] == nums_list[midpoint]:
            right = midpoint - 1
        else:
            cache[midpoint] = midpoint
            return midpoint
    elif nums_list[midpoint] > target:
        right = midpoint - 1
    else:
        left = midpoint + 1

    result = search_first(nums_list, target, left, right)
    cache[midpoint] = result
    return result


def search_second(
    nums_list: List[int], target: int, left: int, right: int, cache={}
) -> int:
    midpoint = (left + right) // 2

    if midpoint in cache:
        return cache[midpoint]

    if left == right and nums_list[midpoint] != target:
        return -1

    if nums_list[midpoint] == target:
        if nums_list[midpoint + 1] == nums_list[midpoint]:
            left = midpoint + 1
        else:
            cache[midpoint] = midpoint
    elif nums_list[midpoint] > target:
        right = midpoint - 1
    else:
        left = midpoint + 1

    value = search_second(nums_list, target, left, right)
    cache[midpoint] = value
    return value


if __name__ == "__main__":
    print(search(list(range(3000)), 2992))
    print(search([1, 2, 2, 3, 3, 4, 5], 3))
    print(search([1, 2, 3, 3, 3, 4, 5, 5, 7, 8, 9], 6))
    print(search([], 5))
    print(search([5, 7, 7, 8, 8, 10], 6))
    # print(search([5], 5))
