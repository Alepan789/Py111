from typing import Optional, Sequence


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""

	def prefix_fun(prefix_str: str) -> Sequence[int]:
		"""
		Prefix function for KMP

		:param prefix_str: substring for prefix function
		:return: prefix values table
		"""

		res = [0]
		for i in range(2, len(prefix_str) + 1):
			_index = 0
			patt = prefix_str[0:i]
			for j in range(1, len(patt) - 1):
				pref = patt[:j]
				suff = patt[-j:]
				if pref == suff:
					_index = j
				# print(f'i:{i} j:{j}  pref:{pref}; suff:{suff} index:{_index} ')
				j += 1
			res.append(_index)
		return res

	# паттерн "переходов"
	pattern = prefix_fun(substr)

	i, j = 0, 0
	while i < len(inp_string):
		# print(f'i:{i} j:{j}  p1:{inp_string[i]} p2:{substr[j]} ')
		if inp_string[i] == substr[j]:
			i += 1
			j += 1
			if j == len(substr):
				print(f'Результат: {i - len(substr)};  str1:{inp_string}  substring:{substr}')
				return i - len(substr)
		elif j <= 0:
			i += 1
		else:
			j = pattern[j - 1]

	print(f'не найдено  str1:{inp_string}  substring:{substr}')


# return None


str_1 = 'qweAAAqweй'
str_2 = 'qwer'
# str_2 = 'ababc'

# str_2 = 'ATATC'
# Итог: f = [0, 0, 1, 2, 0]

# str_2 = 'ATAATA'
# f = [0, 0, 1, 1, 2, 3]

print(kmp_algo(str_1, str_2))

haystack = "Hello, tiny world!"
needle = "Hell"
#
# # haystack = "All these moments will be lost in time..."
# # needle = "time..."
# # 34
# # haystack.index(needle)
print(kmp_algo(haystack, needle))
