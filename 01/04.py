'''Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.'''

n = int(input('Введите целое положительное число:'))

max_n = 0

while n > 0:
    last_n = n % 10
    if last_n > max_n:
        max_n = last_n
    n = n // 10
print('Самая большая цифры в числе: ', max_n)