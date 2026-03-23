# логические операторы

print(True or False) # 1 + 3 = 4 // true
print(False or True) # true
print(1 or 0) # 1
print(1 or 2 or 3) # 1
print(True or hahaha) # True но ошибка остается 
print(None or False or 0) # 0

print(False and True) # false
print(1 and 0) # 0
print(0 and None and False) # 0
print(0 and hahahah) # 0 но ошибка так же остается
print(-2 and 1 and 3) # 3

print(1 > 0 and 10 < 100) # True
print(1 > 0 or 1 > 10)# true

print(1 > 0 or None and '0') # 1 > 0 or False -> true 

# print(5 + 5 or None and 1 > 0) # 10
# print(17 % 3 and -1000 and 2 ** 3) # 8
# print('0' or 0 and 123) # 0

# x = int(input('введите координату x: '))
# y = int(input('введите координату y: '))
# z = int(input('введите координату z: '))

# print(x == 100 and y == 150 and z == 50 and "you luse")


# a = int(input('введите сторону а: '))
# b = int(input('введите сторону b: '))
# c = int(input('введите сторону с: '))

# print(a + b > c and b + c > a and c + a > b)


# a = int(input('введите координату а: '))

# print(a < 50 or a > 100)