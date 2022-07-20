# Анонимные, lambda функции

def sum(x, y):                   # sum = lambda x, y: x + y
    return x + y

f = sum
# f = lambda q, w: q + w

def mylt(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(mylt, 4, 5)
calc(f, 4, 5)
calc(lambda x, y: x + y, 4, 5)

# List Comprehension

list1 =[ i for i in range(1, 21) if i % 2 == 0]    
print(list1)                                          # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def f(x):
    return x**3

list1 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list1)  # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]

# Задача: Из последовательности чисел выбрать четные и составить список пар (число, квадрат числа).
# Пример: 1 2 3 5 8 15 23 38 -> [(2, 4), (8, 64), (38, 1444)]

def select(f, col):
        return [f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)                           # [1, 2, 3, 5, 8, 15, 23, 38]
res = where(lambda x: not x % 2, res)             # [2, 8, 38]
res = select(lambda x: (x, x ** 2), res)          # [(2, 4), (8, 64), (38, 1444)]
print(res)

# Функция map (встроенная функция ЯП вместо select в задаче выше)

li = [x for x in range(1, 20)]
li = list(map(lambda x: x + 10, li))
print(li)                             # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

data = list(map(int, input().split()))
print(data)

# Функция filter (встроенная функция ЯП вместо where в задаче выше)

data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res)                                     # [0, 2, 4, 6, 8]

# Функця zip

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids))   # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
print(data)

data = list(zip(users, ids, salary))
print(data)                           # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]

# Функция enumerate

data = list(enumerate(users))
print(data)                         # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

