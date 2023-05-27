# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)
# [0, -1, 5, 2, 3]
# -> 2 (-1 < 5, 2 < 3)

from random import randint

n = int(input('Введите количество чисел в массиве: '))

numbers = []
for i in range(n):
    numbers.append(randint(1, 9))
print(numbers)

sum = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        sum += 1
        print(f'{numbers[i-1]} < {numbers[i]}')
print(f'Количество чисел = {sum}')
