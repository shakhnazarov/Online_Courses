import bisect
# def binary_search(nums, q):
#     if nums[-1] > q:
#         return "NO SOLUTION"
#     left = 0
#     right = len(nums)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == q:
#             return mid + 1
#         elif nums[mid] < q:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return mid + 1

n, m = map(int, input().split())

nums = list(map(lambda x: -1*int(x), input().split()))

for i in range(m):
    q = int(input())
    res = bisect.bisect_left(nums, -1*q) + 1
    print( res if res <= n else "NO SOLUTION")


# Выдаёт TL




'''
Скаут футбольного клуба «Гарун-Аль-Рашид Сити» выстроил
n
 кандидатов в основу клуба в ряд, отсортировав их по невозрастанию коэффициента защитной эффективности (целое число от
−
1
0
9
 до
1
0
9
, чем меньше, тем лучше) слева направо.
После чего скаут должен отвечать на запросы тренера «у какого самого левого игрока коэффициент меньше либо равен заданному коэффициенту
q
». Игроки пронумерованы слева направо, начиная с единицы.

Формат ввода
В  первой строке записаны два целых числа
n
,
m
 (
1
≤
n
,
m
≤
2
⋅
1
0
5
) — количество кандидатов в основу клуба и количество запросов.
Во второй строке записаны
n
 целых чисел в невозрастающем порядке, каждое по абсолютной величине не превышает
1
0
9
 — коэффициенты защитной эффективности игроков.
В следующих
m
 строках даны запросы. Каждый запрос содержит одно целое число
q
, по абсолютной величине не превышающее
1
0
9
.

Формат вывода
Для каждого запроса выведите минимальный номер футболиста с коэффициентом защитной эффективности, меньшим
q
. Если такого футболиста в распоряжении скаута нет, вместо номера выведите «NO SOLUTION» (без кавычек).
'''