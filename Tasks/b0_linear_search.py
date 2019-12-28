"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	if len(arr) == 0:
		print("упс")
		return

	i = 0
	min_index = 0
	min_value = arr[0]
	while i < len(arr) - 1:
		i += 1
		if arr[i] < min_value:
			min_value = arr[i]
			min_index = i


	print(f"arr:{arr},\nmin:{min_value}; index:{min_index}")
	return min_index