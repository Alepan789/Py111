from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	rez = 0
	i = -1
	print(f"len:{len(stairway)}")
	rez_path = []

	while i < len(stairway) - 1:
		# sum1, sum2 = 0, 0
		print(f"p1 i={i}; step1:{stairway[i]}, step2:{stairway[i + 1]} rez:{rez}")
		if i + 5 <= len(stairway) - 1:
			sum1 = stairway[i + 1] + stairway[i + 2] + stairway[i + 3]
			sum1 = stairway[i + 1] + stairway[i + 2] + stairway[i + 4] + sum1
			sum2 = stairway[i + 2] + stairway[i + 3] + stairway[i + 4]
			sum2 = stairway[i + 2] + stairway[i + 3] + stairway[i + 5] + sum2
		elif i + 4 <= len(stairway) - 1:
			sum1 = stairway[i + 1] + stairway[i + 2] + stairway[i + 3]
			sum1 = stairway[i + 1] + stairway[i + 2] + stairway[i + 4] + sum1
			sum2 = stairway[i + 2] + stairway[i + 3] + stairway[i + 4]
			sum2 = stairway[i + 2] + stairway[i + 3] + sum2

		elif i + 3 <= len(stairway) - 1:
			sum1 = stairway[i + 1] + stairway[i + 2] + stairway[i + 3]
			sum1 = stairway[i + 1] + stairway[i + 2] + sum1
			sum2 = stairway[i + 2] + stairway[i + 3] + stairway[i + 4]

		elif i + 1 <= len(stairway) - 1:
			sum1 = stairway[i]
			sum2 = stairway[i + 1]

		if sum1 < sum2:
			rez_path.append([i + 1, stairway[i + 1]])
			rez += stairway[i + 1]
			print(f"p2 i={i + 1}; step1:{stairway[i]}, step2:{stairway[i + 1]} rez:{rez} sum1:{sum1} sum2:{sum2}  step:{i + 1}:{stairway[i]}\n")
			i += 1
		else:
			rez_path.append([i + 2, stairway[i + 2]])
			rez += stairway[i + 2]
			print(f"p2 i={i + 2}; step1:{stairway[i]}, step2:{stairway[i + 1]} rez:{rez} sum1:{sum1} sum2:{sum2} step:{i + 2}:{stairway[i + 1]}\n")
			i += 2

	print(rez, rez_path)
	return rez


# stairway = (1, 2, 3, 4, 1, 2, 3, 4, 6, 7)
# stairway = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
stairway = [4, 4, 3, 2, 3, 4, 5, 9, 1, 2, 4, 2]
# stairway = [3, 4, 5, 9, 1]

stairway_path(stairway)
