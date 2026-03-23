from random import randint

# score = int(input('счет: ')) 
# if score < 30:
#     print('учись играть, нубик!')
# elif score <= 50:
#     print('чел, норм')
# elif score <= 100:
#     print('чел, харооош')
# else:
#     print('ема ты машина')
#####################333333############################################

'''
NORMAL_TEMP = 36.6

temp = float(input('введите температуру тела: '))

if temp == 36.6:
    print('ты зоров чувааак')
elif temp > 36.9:
    print(f'температура выше нормы на: {round(temp - NORMAL_TEMP, 1)}')
elif temp < 36.3:
    print(f'температура ниже нормы на: {round(NORMAL_TEMP - temp, 1)}')
else:
    print('ну ты в норме')
'''

# a = int(input('A: '))
# b = int(input('B: '))

# if a < b:
#     print(a)
# else:
#     print(b)
'''
constPassword = "123qwe"
constName = "admin"

name = input('введите логин: ')

if constName == name:
    password = input('введите пароль: ')
    if password == constPassword:
        print('добро пожаловать')
    else:
        print('пароль не верный')
else:
    print('такого пользователя нет или не верный логин')
'''
############################################################################

print('я - бот! я загадаю число от 1 до  5, а ты попробуй отгадать!')
value = randint(1, 5)
result = int(input('твой ответ: '))

if value == result:
    print('о, ты угадал!')
else:
    print(f"нет я загодал число {value}, попробуй еще раз)")