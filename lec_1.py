import numbers
from operator import inv


print('hello world')

# типы данных и переменная
# int, float, boolean, str, list, None
value = None
print(type(value))
a = 123
b = 1.23
print(a)
print(type(a))
print(b)
print(type(b))
value = 12334
print(value)
print(type(value))
s = 'hello \n"world"'
print(s)
print(type(s))

print(a, b, value)
print(a, '-',b, '-',value)
print('{} - {} - {}'.format(a, b, value))
print(f'{a} - {b} - {value}')
print('{1} - {2} - {0}'.format(a, b, value))

f = True
print(f)
t = False
print(t)

lis = ['1', '2', '3', 'hello']
print(lis)

# Ввод и вывод данных
# print, input
print('Введите a')
a = input()                   # a = int(input())         a = float(input())
print('Введите b')
b = input()                   # b = int (input())        b = float(input())
print(a, '+', b, '=', a + b)  # 10 + 20 = 30             1.23 + 2.34 = 3.57
print('{} {}'.format(a, b))
print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# ** возведение в степень, // целочисленное деление, % остаток от деления
# Сокращенные операции +=, *=
a = 2        # a = 1.312312
b = 800      # b = 3
c = a ** b   # c = round(a * b, 5)
print (c)    # 3.93694

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
print(a)
func =1
T = 4
x = 123
print(func<T>(x))
f = 1 > 2 or 4 < 6
print(f)
col = [1, 2, 3, 4]
print(2 in col)            # print(not 2 in col) -> False
is_odd = col[0] % 2 == 0   # is_odd = not col[0] % 2 -> False
print(is_odd)

# Управляющие конструкции
# if, if -else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША !')
elif username == 'Марина':
    print('Я так ждал Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

# while, while - else

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит')
print(inverted)

# for

for i in 1, 2, 3, 4, 5:    # list = [1, 2, 3, 4, 5]
    print(i**2)            # for i in list:
r = range(10)
for i in r:                # for i in range(10):       range(1, 10, 2) от 1 до 10 приращение 2
    print(i)
for i in 'qwer-ty':
    print(i)

# Немного о строках

text = 'съешь ещё этих мягких французских булок'
print(len(text))                   #39
print('ещё' in text)               # True
print(text.isdigit())              # False
print(text.islower())              # True
print(text.replace('ещё', 'ЕЩЁ'))  # 'съешь ЕЩЁ этих мягких французских булок'  

help(int)                          # справка языка

for c in text:
    print(c)

print(text[0])                           # с
print(text[1])                           # ъ
#print(text[len(text)])                  # IndexError: string index out of range
print(text[len(text)-1])                 # к
print(text[-5])                          # б
print(text[:])                           # съешь ещё этих мягких французских булок
print(text[:2])                          # съ
print(text[len(text)-2:])                # ок
print(text[2:9])                         # ешь ещё
print(text[6:-18])                       # ещё этих мягких
print(text[0:len(text):6])               # сеикакл
print(text[::6])                         # сеикакл
text = text[2:9] + text[-5] + text[:2 ]  # print(text) -> ешь ещёбсъ

# Списки

numbers = [1, 2, 3, 4, 5]          
print(numbers)                     # [1, 2, 3, 4, 5]
print(type(numbers))               # <class 'list'>
ran = range(1, 6)
print(type(ran))                   # <class 'range'>
numbers = list(ran)
print(type(numbers))               # <class 'list'>
print(numbers)                     # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)                     # [10, 2, 3, 4, 5]
print(len(numbers))                # 5
for i in numbers:
    i *= 2
    print(i)                       # 20 4 6 8 10 
print(numbers)                     # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)                                       # red green blue
for e in colors:
    print(e*2)                                     # redred greengreen blueblue
colors.append('gray')
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red')                               # удаление элемента
print(colors)                                      # ['green', 'blue', 'gray']
del colors[0]                                      # удаление элемента
print(colors)                                      # ['blue', 'gray']
