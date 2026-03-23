# list  26 урок ***********************************************
from functools import reduce
from random import randint

values = [10, 20, 30, 40, 50,]

# получение элемнта списка
print(values[0]) # 10 
print(values[4]) # 50
print(values[-1]) # 50
print(values[-5]) # 10
print(values[1:-1]) # [20, 30, 40]
print(values[1:]) # [20, 30, 40, 50]
print(values[0:-1]) # [10, 20, 30, 40]


# изменение списка
values[0] = 100

print(values) # [100, 20, 30, 40, 50]


# добавление 
values.append(60) # добавление в конец списка
values.insert(0, 10) # до индексу
values.extend([70, 80, 90]) # в конц списка несколько элементов
# print(values)

# удаление
values.pop() # удаление поcледнего элемента
values.pop(1) # удалегние по индексу
values.remove(40) # удаление по значению
print(values)

# домашка
def changeValues(lst):
    a = int(input('введите число A: '))
    b = int(input('введите число B: '))
    lst.insert(0, a)
    lst.append(b)

# changeValues(values)
print(values)

# урок 27********************************************************


# перебор списка
users = ['Alex', 'Marie', 'Bob', 'Jhon']

for user in users:
    print(f'Hello, {user}!')



# колличество элементов списка
print(len(values))

[alex, marie, bob, john] = users
print(john, alex) # John Alex

print(users) # ['Alex', 'Marie', 'Bob', 'Jhon']


# фильтрация списка
def filt1(lst):
    newLst = []
    for elem in lst:
        if elem >= 30:
            newLst.append(elem)
    return newLst


vls1 = filt1(values)
print(vls1)


# урок 28********************************************************
def filt2(lst):
    newLst = []
    for elem in lst:
        if elem % 2:
            newLst.append(elem)
    return newLst


vls2 = filt2([1, 2, 3, 4, 5])
print(vls2) # [1, 3, 5]


def filt3(lst):
    newLst = []
    for elem in lst:
        if len(elem) >= 2:
            newLst.append(elem)
    return newLst


vls3 = filt3(['John', 'Marie', 'Li', 'Alex', 'X', 'Y'])
print(vls3) # ['John', 'Marie', 'li', 'Alex']



def filt(f, lst):
    newLst = []
    for elem in lst:
        if f(elem):
            newLst.append(elem)
    return newLst

vls1 = filt(lambda elem: elem > 30, values)
print(vls1) # [50, 60, 70, 80]
print(type(vls1))
print(filt(lambda elem: elem % 2, [1, 2, 3, 4, 5])) # [1, 3, 5]

vls3 = filt(lambda elem: len(elem)>= 2, ['John', 'Marie', 'Li', 'Alex', 'X', 'Y'])
print(vls3) # ['John', 'Marie', 'li', 'Alex']
# вот это уже отдельная функция, которая работает без вышеупомянутых функций.
# а вышестоящая функция это то как работает функция встроенный в пайтон
vls1 = list(filter(lambda elem: elem > 30, values))
print(vls1) # [50, 60, 70, 80]
print(list(filter(lambda elem: elem % 2, [1, 2, 3, 4, 5]))) # [1, 3, 5]

vls3 = list(filter(lambda elem: len(elem)>= 2, ['John', 'Marie', 'Li', 'Alex', 'X', 'Y']))
print(vls3) # ['John', 'Marie', 'li', 'Alex']
# то есть это самостоятельная функция фильтрации встроенная в пайтон # конец 28 

# урок 29 *************************************************************
# преобразование списка
vls = [1, 2, 3, 4, 5]

def map1(lst):
    newLst = []
    for num in lst:
        newLst.append(num * 2)
    return newLst


vls2 = map1(vls)
print(vls2) # [2, 4, 6, 8, 10]
print(vls) # [1, 2, 3, 4, 5]


vls3 = ['1', '2', '3', '4', '5']


def map2(lst):
    newLst = []
    for num in lst:
        newLst.append(int(num))
    return newLst


print(map2(vls3)) # [1, 2, 3, 4, 5]
print(map2(['10', '20', '30', '40', '50'])) # [10, 20, 30, 40, 50]



def map_(f, lst):
    newLst = []
    for num in lst:
        newLst.append(f(num))
    return newLst


print(map_(lambda num: int(num), vls3)) # [1, 2, 3, 4, 5] можно lambda убрать полностью и поставить int
print(map_(lambda num: int(num), ['10', '20', '30', '40', '50'])) # [10, 20, 30, 40, 50] и тут тоже

vls2 = map_(lambda num: num * 2, vls)
print(vls2) # [2, 4, 6, 8, 10]


vls2 = map(lambda num: num * 2, vls) # [2, 4, 6, 8, 10]
print(list(vls2)) # [2, 4, 6, 8, 10]

print(list(map(int, vls3))) # [1, 2, 3, 4, 5]
print(list(map(int, ['10', '20', '30', '40', '50']))) # [10, 20, 30, 40, 50]

# урк 30***************************************************************************
# преобразование в список
names = 'alex marie nataly bob'

names_list = names.split(' ')
print(names_list) # ['alex', 'marie', 'nataly', 'bob']

# преобразование списока к строке
names2 = ', '.join(names_list)  # 'alex, marie, nataly, bob
print(names2)

names = ', '.join(names.split(' '))   # 'alex, marie, nataly, bob'
# урок 31**************************************************************************
names = ', '.join(names.split(' '))   # 'alex, marie, nataly, bob'
print('alex'[0].upper() + 'alex'[1:])


users = 'alex marie nataly bob'

u1 = users.split(' ') 
print(u1) # ['alex', 'marie', 'nataly', 'bob']
u2 = list(map(lambda user: user[0].upper() + user[1:], u1))
print(u2) # ['Alex', 'Marie', 'Nataly', 'Bob']
u3 = ', '.join(u2)
print(u3) # Alex, Marie, Nataly, Bob

users = ', '.join(map(lambda user: user[0].upper() + user[1:], users.split(' '))) # затупил
print(users) # Alex, Marie, Nataly, Bob

# урок 32*************************************************************************
emails = ['alex.mail.com', 'marie@mail.com', 'bob@mail.com', 'vasya@mail.com', 'alex.mail.com' ]

# количество вхождений элемента
print(emails.count('alex.mail.com')) #2

# получить индекс элемента 
print(emails.index('marie@mail.com')) #1
print(emails.index('alex.mail.com')) #0

# поиск элемента
print('bob@mail.com' in emails) #True
print('bob@mail.com' not in emails) #false
print('nataly@mail.com' not in emails) #True


# фильтрция emiles
print('@' in 'alex.mail.com') # False
print('@' in 'marie@mail.com') # True

emails = list(filter(lambda email: '@' in email, emails))
print(emails)


# генератор списка урок 33 *******************************************************


lst = [i * 2 for i in range(2, 11) if i % 2]
print(lst) # [6, 10, 14, 18]

lst2 = [1, -2, -3, 4, 0, 5, -6, 7, 8, -9, 10]
lst3 =[i * 2 for i in lst2 if i > 0]
print(lst3) # [2, 8, 10, 14, 16, 20]


# lst4 = []
# for i in range(3):
#     lst4.append(int(input('Entr the number: ')))

# lst5 = [int(input('Entr the number: ')) for i in range(3)] #^^^^^^^^
# print(lst5)


# lst = [[i, j] for i in [1, 2, 3] for j in range(3)] #^^^^^^^^
# print(lst)

# урок 34 **************************************************************
def buildTable(lst, cols):
    # newLst = []
    # for i range(0, len(lst), cols):
    #     newLst.append(lst[i:i+cols])
    # return newList
    return [lst[i: i+cols] for i in range(0, len(lst), cols)]
print(buildTable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], randint(2, 4))) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
# урок 35 ****************************************************************
lst = [1, 2, 3]# копирование объекта по ссылке
lst2 = lst

print(lst == lst2) # True
print(lst is lst2) # True

lst2.append(4)
print(lst) # [1, 2, 3, 4]

lst3 = [*lst] # [1, 2, 3, 4]
print(lst3) 
print(lst3 is lst) # False

lst4 = lst
print(lst4) # [1, 2, 3, 4]

lst = [10, 20, 30]
print(lst4) # [1, 2, 3, 4]

print(lst is lst4) # False
# урок 41 **************************

score = 100
message = 'ti lychshiy' if score >= 80 else 'loh'
print(message)

vls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def the_world(lst):
    new_world = []
    for elem in vls:
        new_world.insert(0, elem)

    return new_world

print(the_world(vls)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(vls) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(reversed(vls))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(vls) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


vls.reverse()
print(vls) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

vls2 = [1, 2, 3, 4, 5]
print(sum(vls2)) # 15

sum_numb = reduce(lambda a, b: a + b, vls2)
print(sum_numb) # 15

print(reduce(lambda a, b: a * b, vls2)) # 120



# сортировка списка # урок 46

lst1 = [1, 3, 2, 6, 5, 4, 9, 7, 8]

lst1.sort()
print(lst1) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# по возрастанию
lst2 = [1, 3, 2, 4, 6, 5]
lst3 = sorted(lst2)
print(lst3) # [1, 2, 3, 4, 5, 6]
print(lst2) # [1, 3, 2, 4, 6, 5]

# сортировка по убыванию
lst4 = sorted(lst2, reverse=True)
print(lst4) # [6, 5, 4, 3, 2, 1]


users = [
    {'id': 1, 'name': 'Vasya', 'age': 25},
    {'id': 2, 'name': 'John', 'age': 16},
    {'id': 3, 'name': 'Bob', 'age': 35},
    {'id': 4, 'name': 'Alex', 'age': 18},
]

print(sorted(users, key=lambda user: user['age']))
print(sorted(users, key=lambda user: user['id'], reverse=True))

