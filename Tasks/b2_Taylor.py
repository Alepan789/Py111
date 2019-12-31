"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series
    # 1 + x/1! + x**2/2! + x**3/3! + ...
    :param x: x value
    :return: e^x value
    """

    def xfact(x):
        i = 1
        rez = 1
        while i <= x:
            rez *= i
            i += 1
        return rez

    diff = 0.0000001  # условие прекращения вычисления ряда
    i = 2
    prev_step = x / xfact(1)
    next_step = x ** 2 / xfact(2)
    rez = 1 + prev_step + next_step
    # print(f'i:{i}\t\tprev:{prev_step}\tnext:{next_step}\tdelta{next_step - prev_step}\tfact:{xfact(i)}')
    while abs(prev_step - next_step) > diff or next_step > diff:
        i += 1
        prev_step = next_step
        next_step = (x ** i) / xfact(i)
        rez += next_step
        # print(f'i:{i}\tprev:{prev_step}\tnext:{next_step}\tdelta{prev_step - next_step}\tfact:{xfact(i)} \tx**i:{x**i} ')
    return rez


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series
    :param x: x value
    :return: sin(x) value
    """

    diff = 0.0000001  # условие прекращения вычисления ряда
    i = 2
    xfactorial = 1 * 2 * 3
    prev_step = x ** 3 / xfactorial
    xfactorial = xfactorial * 4 * 5
    next_step = x ** 5 / xfactorial
    rez = x - prev_step + next_step
    # print(f'i:{i}\t\tprev:{prev_step}\tnext:{next_step}\tdelta{next_step - prev_step}\tfact:{xfactorial}')
    while abs(prev_step - next_step) > diff or next_step > diff:
        i += 1
        # ii = i*2+1
        xfactorial = xfactorial * (i * 2) * (i * 2 + 1)
        prev_step = next_step
        next_step = ((-1) ** i) * (x ** (2 * i + 1) / xfactorial)
        rez += next_step
        # print(f'i:{i}\tprev:{prev_step}\tnext:{next_step}\tdelta{prev_step - next_step}\tfact:{xfactorial} \tii:{ii} ')

    return rez
