"""
Taylor series - вариант 2
"""

from typing import Union

def ex(x: Union[int, float], accur: float = 0.0000001) -> float:
    """
    Calculate value of e^x with Taylor series
    # 1 + x/1! + x**2/2! + x**3/3! + ...
    :param x: x value
    :param accur: точность вычисления
    :return: e^x value
    """

    i = 2
    #делитель 1!
    prev_step = x / 1

    #делимое
    top_part = x ** 2

    #делитель == 2!
    btm_part = 2

    next_step = top_part / btm_part
    rez = 1 + prev_step + next_step
    # print(f'i:{i}\t\tprev:{prev_step}\tnext:{next_step}\tdelta{next_step - prev_step}\tfact:{xfact(i)}')
    while abs(prev_step - next_step) > accur or next_step > accur:
        i += 1
        prev_step = next_step
        top_part *= x
        btm_part *= i
        next_step = top_part / btm_part
        rez += next_step
        # print(f'i:{i}\tprev:{prev_step}\tnext:{next_step}\tdelta{prev_step - next_step}\tfact:{xfact(i)} \tx**i:{x**i} ')
    return rez


def sinx(x: Union[int, float], accur: float = 0.0000001) -> float:
    """
    Calculate sin(x) with Taylor series
    # x - x**3/3! + x**5/5! - x**7/7! + x**9/9! ...
    :param x: x value
    :param accur: точность вычисления следующего шага
    :return: sin(x) value
    """

    i = 2
    top_part = x ** 3
    btm_part = 1 * 2 * 3
    prev_step = top_part / btm_part
    top_part = top_part * x * x
    btm_part = btm_part * 4 * 5
    next_step = top_part / btm_part
    rez = x - prev_step + next_step
    # print(f'i:{i}\t\tprev:{prev_step}\tnext:{next_step}\tdelta{next_step - prev_step}\tfact:{xfactorial}')

    while abs(prev_step - next_step) > accur or next_step > accur:
        i += 1
        if i % 2 == 0:
            prefix = 1
        else:
            prefix = -1
        prev_step = next_step
        top_part = top_part * x * x
        btm_part = btm_part * (i * 2) * (i * 2 + 1)
        next_step = prefix * (top_part / btm_part)
        rez += next_step

        # print(f'i:{i}\tprev:{prev_step}\tnext:{next_step}\tdelta{prev_step - next_step}\tfact:{xfactorial} \tprefix:{prefix} ')

    return rez

# import math
# print(ex(2))
# print(sinx(22))
# print(math.sin(22))
