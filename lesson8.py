userName = "Vasya" # глобальная переменная
# урок 18  ********************************************************
# объявление функции
def sayHello():
    userName = "John" # локальная переменная
    print(f'yo bro, {userName}!') 


# # # вызов функции 
sayHello() #  yo bro, John!
sayHello() #  yo bro, John!
sayHello() #  yo bro, John!

print(userName)

def sayHi(userName):
    print(f'yoooo brooo, {userName}!')

sayHi("Петя") # yoooo brooo, Петя!
sayHi("Alex") # yoooo brooo, Alex!
sayHi(userName) # yoooo brooo, vasya!

##########################################################\\\
#изменение глобальной переменной

def editUserName():
    global userName
    userName = input('Введите имя: ')
    print(f'привет {userName}!')


# editUserName()
# print(userName)
# editUserName()
# print(userName)
# editUserName()
# print(userName)
# ##########################################################///
def editUserName(name):
    global userName
    userName = name

editUserName('Alex')
print(userName)
editUserName('Петя')
print(userName)
editUserName('Вася')
print(userName)

##########################################################
#практика # урок 20  ********************************************************
##########################################################

def displayInfo(userName, userAge):
    print(f'Ваше имя: {userName}; Ваш возраст: {userAge}')

# displayInfo('Петя', 20) #ваше имя: Петя, возраст: 20

constLogin = "admin"
constPassword = "123qwe"

def signIn():
    name = input('введите логин: ')
    if constLogin == name:
        password = input('введите пароль: ')
        if password == constPassword:
            print('добро пожаловать')
        else:
            print('пароль неверный')
    else:
        print('логин неверный')


# signIn()


# возврат значения

def calcFactorial(n): # так она принимает значания
    # n = int(input('enter number: ')) # так она ЗАПРАШИВАЕТ значение
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

result = calcFactorial(3) # тут отна ОТДАЕТ значение 
# print(result)
result = calcFactorial(11)
# print(result)


#практика # урок 21  ********************************************************
def sum(x, y):
    return x + y

result = sum(1, 2) # 3
print(result ** 2) # 9

fact = calcFactorial(11)
print(fact) # 39916800, а без return none
#практика # урок 22  ********************************************************
def sqNumber(q):
    return q ** 2

five = sqNumber(5)
print(five)

# # arгументы по умолчанию урок 23 ******************************************

def sayWelcom(userName = 'No name'): # аргумент по умолчанию = 'No name' 
    print(f'Welcom, {userName}!')

sayWelcom('Alex') # Welcom Alex
sayWelcom() # Welcom No name

# именованные аргументы

def displayData(a=0, b=1, c=2):
    print(f'A: {a}, B: {b}, C:{c}')


displayData(8, 9, 4) # A: 8, B: 9, C: 4
displayData() # A: 0, B: 1, C: 2
displayData(5, 6) # A: 5, B: 6, C: 2
displayData(c=10) # A: 0, B: 1, C:10


def mul(a=1, b=1, c=1):
    return a * b * c 


print(mul(2, 4, 5)) # 40
print(mul(2, 2))    # 4
print(mul(6, c=-10))# -60
print(mul())        # 1


# # lambda урок 24 *************************************************
showMassage = lambda: print('Hello')
showMassage() # Hello

double = lambda x: x * 2
print(double(5)) # 10

multipalay = lambda a, b: a * b 
print(multipalay(5, 3)) # 15

def wrapper(f): # f -> sayHello f это ссылка на функцию #f — это переменная, которая ссылается на функцию
    print('Какой-то очень важный код!')
    f()  # f() -> sayHello() а тут уже вызов функции


wrapper(sayHello) # вызова нет () вот этого warpper вызывает функцию а sayHello вызывает
wrapper(lambda: print('goodbye'))


# # замыкание урок 47
# x = 1

# s = lambda a: a + x
# print(s(1)) # 2


# def f():
#     print(x)
#     return x 

# def f2():
#     x = 0
#     return f()

# f2() # c функции f() будет 1


# def increment():
#     i = 0
#     def count():
#         nonlocal i
#         i += 1
#         return i
#     return count
    
# counter1 = increment()
#print(counter1) # <function increment.<locals>.count at 0x7f1c325ad900>
# # урок 48
# print(counter1()) # 1
# print(counter1()) # 2
# print(counter1()) # 3

# i = 0
# def count():
#     global i
#     i += 1
#     return i

# print(count()) # 1
# print(count()) # 2
# print(count()) # 3


# print(counter1()) # 4
# print('aaaaaaaaaaaaaaaaaa')
# #урок 49
# def sum_arg(a):
#     print(a)
#     def f(b):
#         nonlocal a
#         a += b
#         print(a)
#         return f
#     return f 

# sum_arg(1)(2)(3)(4)(5) # 1 3 6 10 15
# counter2 = increment()
# print(counter2()) # 1
# print(counter1()) # 5

# # кортеж аргументов *args урок 50############################
lst = [1, 2, 3]
lst2 = [*lst]
print( lst == lst2) # True
print( lst is lst2) # False


def f(*args):
    print(args) # (1, 2, 3)
    print(type(args)) # <class 'tuple'>
    print(args[0]) # 1
    print(*args) # 1 2 3
    print(sum(args)) # 6
    for i in args:
        print(i)


#f(1, 2, 3)
#f(1, 2, 3, 4, 5)


# # словарь именнованых параметров **kwargs
def f(**kwargs):
    print(kwargs) # {'a': 1, 'b': 2}
    print(type(kwargs)) # <class 'dict'>


f(a=1, b=2)

def display_info(**kwargs):
    print(f"You name: {kwargs['name']}, Yor age: {kwargs['age']}")
    print(kwargs)


display_info(name='Alex', age=22, id=122) # You name: Alex, Yor age: 22
display_info(name='Vasya', age=18, id=123) # You name: Vasya, Yor age: 18


def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(1, 2, 3)
f(a=1, b=2)
f()




# декоратор урок 50######################
# # примеры гпт
# def square():
#     return 5 * 5

# def wrapper(f):
#     print("Считаем...")
#     result = f()
#     print("Готово!")
#     return result

# print(wrapper(square))
# ########
# def decorator(f):
#     def wrapped():
#         print("До")
#         f()
#         print("После")
#     return wrapped

# def hello():
#     print("Привет!")

# hello = decorator(hello)
# hello()



# декоратор урок 50###############################################
def show_welcome(f):
    def wrapper(*args, **kwargs):
        print('Hello!')
        f(*args, **kwargs)
        print('Goodbye!')
    return wrapper


@show_welcome # cокращение от calculator = show_welcome(calculator)
def calculator():
    print(eval(input('Введите умное математическое выражение: ')))

#calculator()


@show_welcome # #checkTarget = show_welcome(checkTarget)
def checkTarget():
    for i in range(3):
        for j in range(3):
            target = int(input(f'TR: {i}; TD: {j} '))
            if target == 10:
                print("Цель поражена")
                return
    print('loh')

#checkTarget()

@show_welcome
def sum_args(a, b):
    print(a + b)

sum_args(1, 2) # show_welcome.<locals>.wrapper() takes 0 positional arguments but 2 were given

# урок 52 #############################################
# dic = {'a': 1, 'b': 2}
# print((1, 2, 3) + tuple(dic.items()))


def cache(func):
    # кеш предыдущих вызовов
    cache_calls = {}

    def wrapper(*args, **kwargs):
        tuple_args = args+ tuple(kwargs.items())
        if tuple_args in cache_calls:
            return cache_calls[tuple_args]
        result = func(*args, **kwargs)
        cache_calls[tuple_args] = result
        return result

    return wrapper


@cache
def sum_all(a=1, b=2, c=3):
    #тяжелый код в качестве примера
    for i in range(10_000_000):
        i += a + b + c
    return i


print(sum_all(10, c=30)) # 10000041
print(sum_all(10, c=30))
print(sum_all(10, c=30))
print(sum_all(10, c=30))
print(sum_all(10, c=30))

print(sum_all(10, 5, c=30)) # 10000044
print(sum_all(10, 5, c=30))
print(sum_all(10, 5, c=30))
print(sum_all(10, 5, c=30))
# повторить 52 урок