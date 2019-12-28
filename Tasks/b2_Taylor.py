"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    # 1 + x/1! + x**2/2! + x**3/3! + ...

    def xfact(x):
        i = 1
        rez = 1
        while i <= x:
            rez *= i
            i += 1
        return rez

    i = 2
    prev_step = x / xfact(2)
    next_step = x ** 2 / xfact(1)
    rez = 1 + prev_step + next_step

    print(f'i:{i}\t\tprev:{prev_step}\tnext:{next_step}\tdelta{next_step - prev_step}\tfact:{xfact(i)}')

    while next_step - prev_step > 0.00000001 :
        i += 1
        prev_step = next_step
        next_step = (x ** i) / xfact(i)
        rez += next_step
        print(f'i:{i}\t\tprev:{prev_step}\t\tnext:{next_step}\t\tdelta{next_step - prev_step}\tfact:{xfact(i)}')

    # print(x)
    return rez


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    return 0


# print(ex(1))
# print(ex(2))
print(ex(1))
# print(ex(4))
