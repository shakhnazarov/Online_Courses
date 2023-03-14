"""
Find neighbors for each coordinate and check whether the graph is bipartite
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(10001)

def bipartite(graph, colors, now, curr_color):
    colors[now], curr_color = (1, 2) if curr_color==1 else (2, 1)

    for neigh in graph[now]:
        if colors[neigh] == colors[now]:
            global is_bipartite
            is_bipartite = False
        if colors[neigh] == 0:
            bipartite(graph, colors, neigh, curr_color)


# read input
N = int(input())
vertexes = []
for i in range(N):
    vertexes.append(tuple(map(int,input().split())))

weights = set()
for i in range(N):
    for j in range(i+1, N):
        x_1, y_1 = vertexes[i]
        x_2, y_2 = vertexes[j]
        weights.add((x_1-x_2)**2 + (y_1-y_2)**2)

weights = sorted(list(weights))

# check whether for this R bipartite graph is possible
# customary bin_search
L = 0
R = len(weights)-1
last_R = 0
colors_ans = {}
while L <= R:
    mid = (L+R)//2
    # each time check whether the graph wih new radius is bipartite
    colors = {}
    for vertex in vertexes:
        colors[vertex] = 0

    # each time construct new graph as neighbors change
    graph = defaultdict(list)
    for i in range(N):
        for j in range(i+1, N):
            x_1, y_1 = vertexes[i]
            x_2, y_2 = vertexes[j]
            if (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 < weights[mid]: # if their ranges only touch this is OK (hence <)
                graph[vertexes[i]].append(vertexes[j])
                graph[vertexes[j]].append(vertexes[i])

    # check whether bipartite
    is_bipartite = True
    curr_color = 1
    for vertex in vertexes:  # mights be several components in the graph, need to check each
        if colors[vertex] == 0:
            bipartite(graph, colors, vertex, curr_color)

    if is_bipartite:
        last_R = weights[mid]
        colors_ans = colors
        L = mid + 1
    else:
        R = mid - 1

# fix output to 9 decimal points (to mitigate errors of 10^-8
print(f'{round(last_R**(1/2)/2, 9):.9f}')
print(*colors_ans.values())

'''
Performance: P 3.11.2 (-); P 3.9 PyPy 7.3.11 (1920 ms, 126.38 Mb)
Complexity: O(N^2*logN)
Auxiliary Space: O(N^2)
Test Cases:
4
0 0
0 1
1 0
1 1
ans: 0.707106781186548 1 2 2 1
'''