from typing import List


def find_last_occurence(nums: List[int], target: int) -> int:
    """Find the position of the last occurence of the target value

    Parameters
    ----------
    nums : List[int]
        List of numbers
    target : int
        Target value to find last occurence

    Returns
    -------
    int
        Last position in list
    """
    if len(nums) == 0:
        return
    index = len(nums) - 1
    while nums[index] != target:
        index -= 1
    return index + 1


print(
    find_last_occurence(
        [0, 2, 4, 2, 5, 6, 8, 2, 6, 3, 4, 5, 6, 3, 2, 2, 7, 8, 9, 1, 2, 2, 1], 2
    )
)
