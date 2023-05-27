# Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В
# последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X. Пример:
# 5
# 1 2 3 4 5
# 6 -> 5

from random import randint

N = int(input('Введите количество чисел в массиве: '))

numbers = []
for i in range(N):
    numbers.append(randint(1, 20))
print(numbers)

X = int(input('Введите искомое число: '))

left = []
rigth = []

for j in range(N):
    if X >= numbers[j]:
        left.append(numbers[j])
    elif X <= numbers[j]:
        rigth.append(numbers[j])
# print(left)
# print(rigth)

minLeft = X - left[0]
ind1 = 0
for k in range(1, len(left)):
    minTempLeft = X - left[k]
    if minTempLeft < minLeft:
        minLeft = minTempLeft
        ind1 = k
# print(left[ind1])

minRigth = rigth[0] - X
ind2 = 0
for c in range(1, len(rigth)):
    minTempRigth = rigth[c] - X
    if minTempRigth < minRigth:
        minRigth = minTempRigth
        ind2 = c
# print(rigth[ind2])

if minLeft < minRigth:
    print(f'Ближайшее по величине число {left[ind1]}')
elif minLeft > minRigth:
    print(f'Ближайшее по величине число {rigth[ind2]}')
else:
    print(
        f'Ближайие по величине числа {left[ind1]} и {rigth[ind2]}')
