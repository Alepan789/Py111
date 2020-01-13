"""
проверка работы ГИТ и тд и тп
"""
import json

biblio = []
# biblio.append({"id":"1", "name":"Война и Мир", "autor":"Л.Н.Толстой"})
biblio.append({"id":"2", "name":"Евгений Онегин", "autor":"А.С.Пушкин"})
biblio.append({"id":"3", "name":"Демон", "autor":"М.Ю.Лермонтов"})
# biblio.append({"id":"8", "name":"Капитанская дочка", "autor":"А.С.Пушкин"})
biblio.append({"id":"4", "name":"Сказка о царе Салтане", "autor":"А.С.Пушкин"})
# biblio.append({"id":"5", "name":"Анна Каренина", "autor":"Л.Н.Толстой"})
# biblio.append({"id":"6", "name":"Крейцерова соната", "autor":"Л.Н.Толстой"})
# biblio.append({"id":"7", "name":"Детство. Отрочество. Юность", "autor":"Л.Н.Толстой"})
# print(biblio)

with open("books_file.txt", "w") as fp:
    json.dump(biblio, fp)
    # for i in biblio:
    #     print(i)
    #     json.dump(i)

file_data = []
with open("books_file.txt", "r") as fp:
    file_data = json.load(fp)
    # for i in range(1):
    #     file_data = json.loads(fp)
print(f"c={file_data}, type:{type(file_data)}")
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


"""    
with open("books_file.txt", "w") as fp:
    json.dump(file_data, fp)
    print(f"c={c}, type:{type(c)}")

with open("books_file.txt", "r") as fp:
    # c = json.loads(fp)
    print(json.loads(fp))
    # print(f"c2={c}, type:{type(c)}")
"""

def find_param(param, find_str):
    res = []
    find_str = find_str.lower()
    for book in file_data:
        str = book[param].lower()
        # print(f"book: {book} parameter:{book[param]} str:{str} findStr:{find_str}")
        if str.find(find_str) != -1:
            res.append(book["id"])
    print(f"findName:{res}")
    return res


find_param("name", 'демон')
find_param("autor", 'Пушкин')