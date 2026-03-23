from functools import reduce
'''
vls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 41

def reversNumber(lst):
    vlsR = []
    for i in lst:
        vlsR.insert(0, i) # т.е мы добавляем первый эл на 0, после 2ой эл в начало
    return vlsR

print(reversNumber(vls))
print(vls)

print(list(reversed(vls)))
print(vls)


vls.reverse()


vls2 = [1, 2, 3, 4, 5]
print(sum(vls2))

simNumb = reduce(lambda a, b: a + b, vls2)
print(simNumb)


simNumb2 = reduce(lambda a, b: a * b, vls2)
print(simNumb2)
'''

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











