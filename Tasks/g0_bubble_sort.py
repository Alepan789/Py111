from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	j = 1
	new_container = list(container)
	no_change = False
	while not no_change:
		no_change = True
		i = 0
		while i < len(container) - 1:
			if new_container[i + 1] < new_container[i]:
				new_container[i], new_container[i + 1] = new_container[i + 1], new_container[i]
				no_change = False
			i += 1
			# print(f'j:{j} i:{i} rez:{no_change} Collection:{new_container}')
		print(f'j:{j} i:{i} rez:{no_change} Collection:{new_container}')
		j += 1
	print(f'\nResult: {new_container} type:{type(container)}\n')
	return new_container



def sort2(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	step = 1
	new_container = list(container)
	no_change = False
	while not no_change:
		no_change = True
		for i in range(len(container) - 1):
			if new_container[i + 1] < new_container[i]:
				new_container[i], new_container[i + 1] = new_container[i + 1], new_container[i]
				no_change = False
			print(f'step:{step} i:{i} rez:{no_change} Collection:{new_container}')
		step += 1
		print('-'*5)
	print(f'\nResult v2: {new_container} \ntype:{type(container)}\n')
	return new_container



def sort_k1(container: Collection[_Tt], k) -> Collection[_Tt]:
	"""
	Поиск K минимумов в массиве (simple)
	"""
	rez = sorted(container)[0:k]
	print(rez)
	return rez


def sort_k2(container: Collection[_Tt], k) -> Collection[_Tt]:
	"""
	Поиск K минимумов в массиве (любым из двух методов, без шаблона)
	"""
	i = 0
	rez = container[0]
	rez = range
	print(rez)

	for i in range(1, len(container) - 1):
		if rez > container[i]:
			rez = container[i]

	print(rez)
	return rez




# a = [4, 5, 3, 2, 1]
# a = frozenset(a)
a = (3, 2, 1)
# a = [4, 5, 3, 2, 1]
# sort(a)
# sort2(a)

a = [4, 5, 6, 7, 5, 3, 2, 1, 5]
# print(a, type(a), set(a), )
sort_k1(a, 3)
sort_k2(a, 3)



# a = [4, 5, 3, 2, 1]
# a1 = a[0]
# a2 = if a[1]
#
# a1 =



