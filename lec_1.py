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

list = ['1', '2', '3', 'hello']
print(list)

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

