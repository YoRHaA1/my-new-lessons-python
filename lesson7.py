from random import randint

# i = 0

# while i <= 5:
#     print(i)    # 0 - 4
#     i += 1      # i = i + 1 == i =1
# #########################################################################
# while True:
#     password = input('введите пароль: ')
#     if password == "123qwe":
#         print('Welcom')
#         break
# #########################################################################
# print('я - бот! я загадаю число от 1 до  5, а ты попробуй отгадать!')

# while True:
#     value = randint(1, 5)
#     result = int(input('твой ответ: '))

#     if value == result:
#         print('о, ты угадал!')
#         break
#     else:
#         print(f"нет я загодал число {value}, попробуй еще раз)")
# #########################################################################

# for i in range(3, 9):
#     print(i) 

# for i in range(1, 10, 2):
#     print(i) # 1 3 5 7 9

# for i in range(10, 0, -1):
#     print(i) 
# #########################################################################
# a = int(input('enter A: '))
# b = int(input('enter B: '))

# if a == b:
#     print(a)
# else:
#     if a < b:
#         step = 1
#     else:
#         step = -1
#     for i in range(a, b + step, step):
#             print(i)
# #########################################################################

# value = int(input('введите число: '))
# print('Hello\n' * value)

# #########################################################################

# n=5
# validPassword = '123qwe'
# for i in range(5):
#     n -= 1
#     userPassword = input('введите пароль: ')
#     if userPassword == validPassword:
#         print('вы вошли на сайт!')
#         break
#     else:
#         print(f'пароль неверный! У вас осталось {n} попыток')
# else:
#     print('ваш аккаунт заблокирован')
# #########################################################################


# r = range(3, 50, 3)
# for i in r:
#     if i % 2:  #удалено != 0
#         print(i)


# n = int(input('enter number: '))
# result = 0
# for i in range(1, n + 1):
#     result += i

# print(result)

# !5 == 5 * 4 * 3 * 2 * 1 есть 5 человек, сколько всего вариантов получится?

# #########################################################################

# n = int(input('enter number: '))

# result = 1
# for i in range(1, n + 1):
#     result *= i
# print(result)

#########################################################################

# continue

# r = range(3, 50, 3)
# for i in r:
#     if i % 2 == 0:
#         continue
#     print(i)

# я остановился на уроке 17
##########################################################################


checkTarget = False
for i in range(3):  # строки
    for j in range(3):  # ячейки
        target = int(input(f'TR: {i}; TD: {j} '))
        if target >= 10:
            checkTarget = True
            print("Цель поражена")
            break 
    if checkTarget:
        break
else:
    print('loh')

#    строка V V V
# ячейка >  # # #
#        >  # # #
#        >  # # #

##########################################################################
###################### урок 22
def checkTarget():
    for i in range(3):
        for j in range(3):
            target = int(input(f'TR: {i}; TD: {j} '))
            if target == 10:
                print("Цель поражена")
                return
    print('loh')

checkTarget()