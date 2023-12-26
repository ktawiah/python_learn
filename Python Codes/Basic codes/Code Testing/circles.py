from math import pi


def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Radius must be an integer or a float")
    if r < 0:
        raise ValueError("Radius of circle cannot be negative")
    return pi * pow(r, 2)


circle_area(-4)
