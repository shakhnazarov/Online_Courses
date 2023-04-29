import sys
sys.setrecursionlimit(100001)

def dfs(graph, visited, now):
    count = 1
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            count += dfs(graph, visited, neigh)
    return count



N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(len(graph))]
visited[0] = True
for i in range(M):
    f, s = map(int, input().split())
    graph[f].append(s)
    graph[s].append(f)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        ans = max(ans, dfs(graph, visited, i))

print(ans)







'''
Вам задан неориентированный граф с
N
 вершинами и
M
 рёбрами (
1
≤
N
≤
2
0
0
0
0
,
1
≤
M
≤
2
0
0
0
0
0
). В графе отсутствуют петли и кратные рёбра.
Найдите компоненту связности заданного графа с наибольшим количеством вершин и выведите соответствующее количество вершин.

Формат ввода
Первая строка входа содержит числа
N
 и
M
. Каждая из следующих
M
 строк содержит описание ребра — два целых числа из диапазона от
1
 до
N
 — номера концов ребра.
Формат вывода
Выведите одно целое число — число вершин в максимальной компоненте связности графа.
'''