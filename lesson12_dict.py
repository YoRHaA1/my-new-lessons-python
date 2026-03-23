# словарь урок 37

values = {1: 10, 2: 20, 3: 30, }

# получение значения
print(values[1]) # 10
print(type(values)) # <class 'dict'>
print(len(values)) # 3

user = {
    'name': 'Vasya',
    'age': 20,
    'isStudent': False
}

print(user['name']) # Vasya


# изменение значения
user['isStudent'] = True
print(user) # {'name': 'Vasya', 'age': 20, 'isStudent': True}

# Добавление значения 
user['country'] = 'Russia'
print(user) # {'name': 'Vasya', 'age': 20, 'isStudent': True, 'country': 'Russia'}

# удаление значения 
del user['country']
print(user) # {'name': 'Vasya', 'age': 20, 'isStudent': True}
# задача
salaries = {
    'Bob': 2000,
    'John': 2500,
    'Marie': 3000
}

for userName in salaries:
    print(userName) # key

for userName in salaries:
    print(salaries[userName]) # value

# урок 38****************************************************
sumSalaries = 0
for userName in salaries:
    sumSalaries += salaries[userName]
print(sumSalaries)


# список ключей
keys = salaries.keys()
print(list(keys)) # ['Bob', 'John', 'Marie']


# список значений
values = salaries.values()
print(list(values)) # [2000, 2500, 3000]

# сумма 
print(sum(values))


phonebook = {
    'Bob': '+123 400 500',
    'John': '+123 400 795',
    'Marie': '+123 400 456',
}

# name = input('введите имя: ')
# print(phonebook[name])


student = {'faculty': 'Medicine', 'course': 3}

user.update(student)
print(user) # {'name': 'Vasya', 'age': 20, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}

print(student) # {'faculty': 'Medicine', 'course': 3}
# # домашка урок 39**************************************************************
users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

def get_user_name(users): # в скобках может быть что угодно написанно, только если оно написанно при вызове
    return list(map(lambda user: user['name'], users))
    # new_list_users = []
    # for user in users:
#         new_list_users.append(user['name'])
#     return new_list_users
print(get_user_name(users)) # ['Vasya', 'Bob', 'Alex']

bob_tel = phonebook.get('Bob', None)
print(bob_tel) # +123 400 500

alex_tel = phonebook.get('Alex', None)
print(alex_tel) # None
# урок 40*******************************************************************

# ДОМАШКА
users2 = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Alex', 'age': 25},
]

def get_new_age(users):
    get_age = 0
    for user in users:
        age = user.get('age', None)
        if not age:
            return 'Возраст пользователя отсутсвует'
        get_age += age
    return get_age / len(users)

# print(get_new_age(users))
awer_age = get_new_age(users)
print(awer_age)


awer_age = get_new_age(users2)
print(awer_age)


user2 = user
print(user) # {'name': 'Vasya', 'age': 20, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}

print(user2 is user) # True
user2['age'] += 1
print(user) # {'name': 'Vasya', 'age': 21, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}

user3 = {**user} # {'name': 'Vasya', 'age': 20, 'isStudent': True, 'faculty': 'Medicine', 'course': 3}
print(user3 is user) # False
print(user == user3) # True
# урок 41  в лессоне 10 





# ключем может быть любой неизменяемый объект