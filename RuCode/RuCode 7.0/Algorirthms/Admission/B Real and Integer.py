def round_corr(num):
    if num > 0:
        return floor(num + 0.5)
    elif num < 0:
        return ceil(num - 0.5)
    else:
        return 0

from math import ceil, floor
num = float(input())

print(floor(num), ceil(num), round_corr(num))


'''
На вход подаётся вещественное число. Требуется его округлить до ближайшего целого, которое его не превосходит, до ближайшего целого, которое его превосходит, и в соответствии с правилами округления (в частности, 0.5 округляется в направлении от нуля), и вывести все три целых числа в указанном порядке.

Формат ввода
Одно вещественное число в интервале от -1000 до 1000 с непустой дробной частью.

Формат вывода
Выведите три целых числа: первое — ближайшее целое, не превосходящее заданного вещественного числа, второе — ближайшее целое, превосходящее заданное вещественное число, третье — ближайшее целое по правилам округления.
'''