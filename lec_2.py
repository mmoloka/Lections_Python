# Файлы

colors = ['red', 'green', 'blue']   # a - открытие для добавленияя данных;
data = open('file.txt', 'a')        # w - открытие для чтения данных; r - открытие для записи данных
data.writelines(colors)             # разделетилей не будет
data.close()

with open('file.txt', 'a') as data:
    data.write('\nline 1\n')
    data.write('line2\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)

# Функции и модули

import lec_1 as l
print(l.f(1))
print(l.f(2.3))
print(l.f(28))

def new_string(symbol, count = 3):
    return symbol * count
print(new_string('!', 5))
print(new_string('!'))
print(new_string(4))

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w'))
print(concatenatio('a', '1', 'd', '2'))

# Рекурсия

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

# Кортежи

a = (3, 4, 5)
print(a)
print (a[1])
for item in a:
    print(item)

t = ()
print(type(t))                                          # tuple
t = (1,)
print(type(t))                                          # tuple
t = (1)
print(type(t))                                          # int
t = (28, 9, 1990)
print(type(t))                                          # tuple
colors = ['red', 'green', 'blue']
print(colors)                                           # ['red', 'green', 'blue']
t = tuple(colors)
print(t)                                                # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0])                                             # red
print(t[2])                                             # blue
print(t[10])                                            # IndexError: tuple index out of range
print(t[-2])                                            # green
print(t[-200])                                          # IndexError: tuple index out of range
for e in t:
 print(e)                                               # red green blue
t[0] = 'black'                                          # TypeError: 'tuple' object does not support item assignment
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))        # r:red g:green b:blue

# Словари

dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary)                             # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
                                              # типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
for k in dictionary.keys():
    print(k)
for v in dictionary.values():                 # for v in dictionary:
    print(v)                                  #     print(dictionary[v])
for v in dictionary:
    print(dictionary[v])
print(dictionary['type'])                     # KeyError: 'type'
del dictionary['left']                        # удаление элемента
for item in dictionary:                       # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))

# Множества

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a))                                  # set
print(type(b))                                  # set
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a))                                  # set
print(type(b))                                  # set
print(type(c))                                  # set
a = {1, 1, 1, 1, 1}
print(a)                                        # {1}

colors = {'red', 'green', 'blue'}
print(colors)                                   # {'red', 'green', 'blue'}
colors.add('red')
print(colors)                                   # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)                                   # {'gray', 'red', 'green', 'blue'}
colors.remove('red')
print(colors)                                   # {'gray', 'green', 'blue'}
colors.remove('red') # KeyError: 'red'
colors.discard('red')                           # ok
print(colors)                                   # {'gray', 'green', 'blue'}
colors.clear()                                  # { }
print(colors)                                   # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                                      # c = {1, 2, 3, 5, 8}
u = a.union(b)                                    # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)                             # i = {8, 2, 5}
dl = a.difference(b)                              # dl = {1, 3}
dr = b.difference(a)                              # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))      # {1, 21, 3, 13}
print(q)

a = {1, 2, 3, 5, 8}
b = frozenset(a)                                  # Неизменяемое множество
print(b)                                          # frozenset({1, 2, 3, 5, 8})

# Списки 

list1 = [1, 2, 3, 4, 5]
list2 = list1
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

list1[0] = 123
list2[1] = 333
for e in list1:
    print(e)
print()
for e in list2:
    print(e)

print(list1.pop())                        # удаляет последний элемент списка
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
print(list1.pop(0))
print(list1)
print(list1.append(11))                  # добавляет элемент в конец списка
print(list1)
print(list1.insert(1, 22))               # вставляет элемент в список перед указанным индексом 
print(list1)



