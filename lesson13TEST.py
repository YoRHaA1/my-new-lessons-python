# кортеж - неизменяемый список

user = ('Alex', 20, 'alex@a.com')
print(user)

user = 'Alex', 20, 'alex@a.com'
print(user)

user2 = ('Alex', )
print(user2)

print(user[0])
print(user[-1])
print(user[:-1])

name, age, email = user
print(email)

# user[0] = 'Tohn'

print(name in user)
print(21 in user)
for i in user:
    print(i)


print(len(user))

def sum_elem(a, b):
    return a + b

results = {
    (1, 2): 3,
    (5, 5): 10,
    ('hello', 'world'): 'helloworld'
}


print(results[(1, 2)])



lst = [1, 2, 3, 4, 5, ]

tp1 = tuple(lst)
print(tp1)

x, y, z = 10, 20, 30
print(y)

def get_data(a, b):
    return a + b, a * b


res = get_data(2, 3)
print(res)

sum_elem, mul_elem = res[0], res[1]

sum_elem, mul_elem = get_data(2, 3)
print(mul_elem)
print(sum_elem)

print(type(res))

data = 123, 
print(data)

numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(numbers[1:-1])
print(numbers[1::-1])
print(numbers[1:-1:2])
print(numbers[:-1:2])
print(numbers[::2])
print(numbers[::-1])
print(numbers[1::-1])
print(numbers[::-2])

