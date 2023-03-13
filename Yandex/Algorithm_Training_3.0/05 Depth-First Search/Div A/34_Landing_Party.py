"""
For each vertex find the minimum point and add to the set of minimum points, note that only one minimum  on the
field of the same minimums will be correct as if troop lands in one of the minimums on the plateau they can  slide
to the trap
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(100001)  # initial limit is usually 1000

DXY = [(1,0), (-1,0), (0,1), (0,-1)]

def has_lower(graph, vertex):
    i, j = vertex
    for dx, dy in DXY:
        if graph[i - dx][j - dy] < graph[i][j]:
            return True
    return False

def has_same(graph, vertex):
    i, j = vertex
    for dx, dy in DXY:
        if graph[i - dx][j - dy] == graph[i][j]:
            return True
    return False

def dfs(graph, visited, now):
    i, j = now
    visited[i][j] = True
    neighs = []
    # may not worry about indexes as they will not be out of bound due to padded field of MAX_HEIGHT+1
    for dx, dy in DXY:
        if graph[i - dx][j - dy] == graph[i][j] and (not visited[i - dx][j - dy]):
            if has_lower(graph, (i - dx, j - dy)):
                global is_plateau
                is_plateau = False
            neighs.append((i - dx, j - dy))

    for neigh in neighs:
        dfs(graph, visited, neigh)



# read input
N, M  = map(int, input().split())
MAX_HEIGHT = 10000
field = [[MAX_HEIGHT+1 for _ in range(M+2)] for __ in range(N+2)]
for i in range(1, N+1):
    field[i][1:M+1] = list(map(int, input().split()))

# use dfs to explore the possible component of descending heights
count = 0
visited = [[False for _ in range(M + 2)] for __ in range(N + 2)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j]:
            is_plateau = True
            if has_lower(field, (i, j)):
                continue
            if has_same(field, (i, j)):
                # Essentially, check whether any of the neighbors with the same height has a lower height
                dfs(field, visited, (i, j))
            if is_plateau:  # is_plateau can be changed in "dfs"
                count += 1

print(count)

'''
Complexity: O((NM)^2)
Auxiliary Space: O(N*M)
Test cases:
1 1
1
ans: 1
2 3
4 4 4
4 4 4
ans: 1
4 4
1 2 4 1
2 4 4 4
1 4 3 2
1 2 3 2
ans: 4
'''