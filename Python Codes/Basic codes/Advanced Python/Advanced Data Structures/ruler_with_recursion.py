from time import time


def draw_ruler(length: int, start=0) -> str:
    """Output ruler markings

    Parameters
    ----------
    length : int
        Length of the ruler
    start : 0
        Start value for keeping the recursion in check

    Returns
    -------
    str
        Ruler markings
    """

    if start > length:
        return

    if start % 1 == 0.25 or start % 1 == 0.75:
        print("-" * 2)

    if start % 1 == 0.5:
        print("-" * 3)

    if start % 1 == 0:
        print(f"{'-'*4} {int(start)}")

    draw_ruler(length, start=start + 0.25)


if __name__ == "__main__":
    start_time = time()
    draw_ruler(50)
    end_time = time()
    print(end_time - start_time)
