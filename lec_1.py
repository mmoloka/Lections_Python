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