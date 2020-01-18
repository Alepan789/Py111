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
			for j in range(1, len(patt)):
				pref = patt[:j]
				suff = patt[-j:]
				if pref == suff:
					_index = j
				# print(f'i:{i} j:{j}  pref:{pref}; suff:{suff} index:{_index} ')
				j += 1
			res.append(_index)
		return res
	# end prefix_fun()

	# паттерн "переходов" заполняем
	pattern = prefix_fun(substr)
	print(f'pattern:{pattern}')

	i = 0
	j = 0
	for i in range(len(inp_string)):
		# print(f'i:{i} j:{j}  p1:{inp_string[i]} p2:{substr[j]} ')
		if inp_string[i] == substr[j]:
			i += 1
			j += 1
			if j == len(substr):
				print(f'Результат: {i - len(substr)};  str1:{inp_string}  \nsubstring:->{substr}<- len:{len(inp_string)}')
				return i - len(substr)
		elif j <= 0:
			i += 1
		else:
			j = pattern[j - 1]

	print(f'не найдено;  str1: {inp_string}  substring: {substr}')
	# end kmp_algo()
	# return None


str_1 = 'qweAAAqweй'
str_2 = 'qwer'
# str_2 = 'ababc'

str_1 = 'ABCDMXYT ABABzCDAB aa'
str_2 = 'ABABC'

str_2 = 'aa'

# str_2 = 'ATATC'
# Итог: f = [0, 0, 1, 2, 0]

# str_2 = 'ATAATA'
# f = [0, 0, 1, 1, 2, 3]

print(kmp_algo(str_1, str_2), '\n')

haystack = "Hello, tiny world!aa"
needle = "Hell"
# needle = 'aa'
#
# # haystack = "All these moments will be lost in time..."
# # needle = "time..."
# # 34
# # haystack.index(needle)
print(f'Индекс результат: {kmp_algo(haystack, needle)}\n')

# str_1 ='Определение: префикс функция – такая функция F(j), что возвращает число, равное максимальной длине префикса строки P[0, j], совпадающего с суффиксом строки '
# # str_2 = 'что'
# # print(kmp_algo(str_1, str_2), '\n')
# # print(str_1.split())
#
# for i in str_1.split():
# 	print(kmp_algo(str_1, i))
