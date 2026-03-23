values = {1:10, 2:20, 3:30,}


print(values[1])
print(type(values)) # <class 'dict'>
print(len(values)) # 3

user = {
    'name': 'Vasya',
    'age': 20,
    'isStudent': False,
}

print(user['name'])

user['isStudent'] = True
print(user)

user['country'] = 'Russia'
print(user)

del user['country']
print(user)


salaries = {
    'Bob': 2000,
    'John': 2500,
    'Marie': 3000
}


n = 0
for name in salaries:
    n += salaries[name]

print(n)



keys = salaries.keys()
print(list(keys))



values = salaries.values()
print(list(values))


print(sum(values))


phonebook = {
    'Bob': '+123 400 500',
    'John': '+123 400 795',
    'Marie': '+123 400 456',
}


# print(phonebook[input('Enter Name: ')])


student = {'faculty': 'Medicine', 'course': 3}

user.update(student)
print(user)


users = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 21},
    {'id': 3, 'name': 'Alex', 'age': 25},
]


def get_user_names(use):
    new_list_users = []
    for user in users:
        new_list_users.append(user['name'])
    return new_list_users 
    # return list(map(lambda user: user['name'], users))

    # n = 0  # средний возраст
    # d = len(users)
    # for i in users:
    #     n += i['age']
    # return n / d # средний возраст


print(get_user_names(users))


bob_tel = phonebook.get('Bob', None)
print(bob_tel)

alex_tel = phonebook.get("Alex", None)
print(alex_tel)


users2 = [
    {'id': 1, 'name': 'Vasya', 'age': 20},
    {'id': 2, 'name': 'Bob', },
    {'id': 3, 'name': 'Alex', 'age': 25},
]



def aeg(users):
    n = 0
    for i in users2:
        age = i.get('age', None)
        if not age:
            return "возраста нет"
        n += age
    return n / len(users)


gg = aeg(users2)
print(gg)


user2 = user
print(user)

print(user2 is user)
user2['age'] += 1
print(user['age'])

user3 = {**user}
print(user3 is user)
print(user3 == user)














