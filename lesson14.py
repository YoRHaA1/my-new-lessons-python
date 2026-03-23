# множества -- структура данных для уникальных значений 
# set урок 44

values = {1, 2, 3, 1, 2, 3}
print(values) # {1, 2, 3}

s = {2, 1, 4, 6, 8, 5}
print(s) # {1, 2, 4, 5, 6, 8}

# print(s[0]) #  'set' object is not subscriptable


s = {}
print(type(s)) # <class 'dict'>

s = set()
print(type(s)) # <class 'set'>

lst = [1, 2, 3, 6, 4]
s  = set(lst)
print(s) # {1, 2, 3, 4, 6}

lst1 = list(s)
print(lst1) # [1, 2, 3, 4, 6]


# получение элементов
for elem in s:
    print(elem)

print(3 in s) # true
print(5 in s) # false

# добавление элементов
s.add(5)
print(s) # {1, 2, 3, 4, 5, 6}

# удаление элемента
s = {1, 3, 9, 4, 6, 5, 7, 9, 1}
print(s.pop()) # 1
print(s) # {3, 4, 5, 6, 7, 9}

s.remove(4)
print(s) # {3, 5, 6, 7, 9}
# s.remove(4) # KeyError: 4

s.discard(4)
s.discard(9)
print(s) # {3, 5, 6, 7}

def set_uniq_values(lst):
    return list(set(lst))


lst = [3, 2, 1, 4, 1, 2, 3]
print(set_uniq_values(lst)) # [1, 2, 3, 4]
print(lst)


s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 6, 7, 8}

# пересечение множеств
print(s1.intersection(s2)) # {1, 3}

# объединение множеств
s3 = s1.union(s2)
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1) # {1, 2, 3, 4, 5}

# обновление множеств
s1.update(s2)
print(s1) # {1, 2, 3, 4, 5, 6, 7, 8}

# разность
s4 = s3.difference(s2)
print(s4) # {2, 4, 5}

print(s2) # {1, 3, 6, 7, 8}
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8}




# Домашка 

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 6, 7, 8}

def get_inner_table(set1, set2):
    return list(set1.intersection(set2))


result = get_inner_table(s1, s2)
print(result) # [1, 3]
print(s1)
print(s2)



