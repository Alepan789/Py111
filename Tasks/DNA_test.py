""""
5.	Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях. Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку
"""
a = 	['ATTA']
a.append('ACTA')
a.append('AGCA')
a.append('ACAA')
a.append('ACTA')
# print(a, len(a[0]))
# print(a[0][0])

s2 = ''
for v in a:
	s2 += v
s2 = set(s2)
# print(s2)
# s = list(['' + v for v in a])

# print(f"s:{s}")
b = [{v: 0 for v in s2} for _ in range(len(a[0]))]
# print(b)

res = ''
for i in range(len(a[0])):
	for v in a:
		b[i][v[i]] += 1
		# print(i, v, b[i], v[i])

	maxv = 0
	print(b[i], type(b[i]))

	for key, val in b[i].items():
		# print(key, b[i][key])
		if b[i][key] > maxv:
			maxv = b[i][key]
			ress = key
	res += ress

print(f"res:{res}")



# for i in range(len(a[0])):
# 	print(max(b[i].values()))




