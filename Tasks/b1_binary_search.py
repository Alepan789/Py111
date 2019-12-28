from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    # print(f'На входе arr:{arr} Len:{len(arr)}')

    if len(arr) == 0:
        return
    start_index = 0
    if len(arr) > 1:
        end_index = len(arr)
    else:
        end_index = 0
    res_index = 0
    i = 1
    mdl_index = 0

    while True:
        # print(f"EndIndex:{end_index};  \tstart_index:{start_index}; \tarr:{arr[start_index:end_index]}")
        mdl_index = (end_index - start_index) // 2 + start_index
        if elem == arr[mdl_index]:
            # res_index = (end_index - start_index)//2
            # print(f'res = {elem} за {i+1} шагов index:{mdl_index}')
            return mdl_index
        if elem < arr[mdl_index]:
            end_index = mdl_index
            # arr2 = arr2[0:end_index]
        else:
            start_index = mdl_index + 1
            # arr2 = arr2[end_index + 1:]
        i += 1

        if start_index >= end_index:
            # print(f'Result end_index:{end_index}; start_index:{start_index}; arr:{arr[start_index:end_index]}; искали:{elem} index:{res_index}')
            return
    # print(elem, arr)
    return None

#
# a = 7
#
# b = [1, 3, 5, 7, 9, 5, 17, 19, 23, 99]
#
# b = [1, 2, 3, 4, 5, 6, 7]
# b = [1, 7, 9]
# # b = [1]
# # print(b)
#
# print(binary_search(9, b))
