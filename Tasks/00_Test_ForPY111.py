"""
проверка работы ГИТ и тд и тп
1. выбор - поиск/добавление/выход
2. поиск
2.1 по результату - редактирование, удаление, выход
3. добавление, по результату пп1 и по кругу

"""
import json

params = ('name', 'autor', 'year')

biblio = []
# biblio.append({"id":"1", "year":1990, "name":"Война и Мир", "autor":"Л.Н.Толстой"})
biblio.append({"id": "2", "year":2002, "name": "Евгений Онегин", "autor": "А.С.Пушкин"})
biblio.append({"id": "3", "year":2014, "name": "Демон", "autor": "М.Ю.Лермонтов"})
# biblio.append({"id":"8", "year":1993, "name":"Капитанская дочка", "autor":"А.С.Пушкин"})
biblio.append({"id": "4", "year":1999, "name": "Сказка о царе Салтане", "autor": "А.С.Пушкин"})
# biblio.append({"id":"5", "year":1990,"name":"Анна Каренина", "autor":"Л.Н.Толстой"})
# biblio.append({"id":"6", "year":1990,"name":"Крейцерова соната", "autor":"Л.Н.Толстой"})
# biblio.append({"id":"7", "year":1990,"name":"Детство. Отрочество. Юность", "autor":"Л.Н.Толстой"})
# print(biblio)

with open("books_file.txt", "w") as fp:
    json.dump(biblio, fp)

file_data = []
with open("books_file.txt", "r") as fp:
    file_data = json.load(fp)

print(f"len:{len(file_data)}; c={file_data}, type:{type(file_data)}")
# print(type(file_data))
# print(f" f1:{file_data[1:3]['name']} ")
#     print(f"f2:{file_data[0:2]}")
#     print(f"f3:{file_data[1].values()}")
#     print(f"f4:{file_data[1]['id']}")

i = file_data[1]
# for i in file_data:
#     print(f"i:{i} type:{type(i)} ")
#     print(f"name:{i['name']}")

# print(i["name"])
print(i.keys(), i.values(), i.items())

def edit_book(id, param, value):
    file_data[id][param] = value
    print('Обновление произведено')
    return


def find_param(param, find_str):
    res = []
    resstr = []
    find_str = find_str.lower()
    for i in range(len(file_data) - 1):
        str = file_data[i][param].lower()
        # print(f"book: {book} parameter:{book[param]} str:{str} findStr:{find_str}")
        if str.find(find_str) != -1:
            res.append(i)
            resstr.append({i:(file_data[i]['name'],file_data[i]['autor'],file_data[i]['year'])})
            # res.append({param:book["id"]})
    print(f"Найдено:{resstr}")
    return res


find_param("name", 'демон')




def select_find():
    _str = ''
    while True:
        print('1:название;\t2:автор;\3:год выпуска')
        _parnum = ''
        i = 0
        while _parnum not in ('1', '2', '3') and i < 10:
            i += 1
            _parnum = input('Введите номер параметра   ("x" для выхода)')
            if _parnum in ('x', 'х'):
                print("Выход из поиска")
                return
        if _parnum not in ('1', '2', '3'):
            print('Столько ошибаться нельз, Вам не рекомендуется пользоваться библиотекой')
            return
        _parval = input('Введите значение параметра   ("x" для выхода)')
        if _parval in ('x', 'х'):
            print("Выход из поиска")
            return
        find_param(params(int(_parnum)-1), _parval)
        # elif _parnum == 2:
        #     find_param("name", _parval)
        # else find_param("year", _parval)


def main_menu():
    _str = ''
    while True:
        print('ВЫБЕРИТЕ пункт\n 1:поиск;\t2:добавление;\3/x:выход')
        _parnum = ''
        i = 0
        while _parnum not in ('1', '2', '3', 'x', 'х') and i < 10:
            i += 1
            _parnum = input('Введите номер параметра   ("x" для выхода)')
            if _parnum in ('3', 'x', 'х'):
                print('Выход из программы')
                return
        if _parnum not in ('1', '2', '3'):
            print('Столько ошибаться нельз, Вам не рекомендуется пользоваться библиотекой')
            return
        _parval = input('Введите значение параметра   ("x" для выхода)')
        if _parval in ('x', 'х'):
            return


find_param("autor", 'Пушкин')

edit_book(1, 'autor', 'Лермонтов New')
print(file_data[1])
print(type(file_data),file_data)
print(file_data.pop(0))
print("rez")
print(f"red:{file_data}")


