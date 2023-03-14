"""
Use dfs, but change the direction of edges as in initial setup 1st vertex is not an initial point
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, now):
    graph[now][0] = 1
    for neigh in graph[now][1]:
        if graph[neigh][0] == 0:
            dfs(graph, neigh)
    reachable.append(now)

# Read input
N, M = map(int, input().split())
# Build adjacency list
graph = [[0, set()] for _ in range(N+1)]  # "set" as edges can be multiple
for _ in range(M):
    s, f = map(int, input().split())  # need to invert edges as to find wherefrom 1st is reachable
    if f != s:  # do not add loops
        graph[f][1].add(s)

# Use dfs ti find all reachable vertexes from 1st one
reachable = []
dfs(graph, 1)

print(*sorted(reachable))

'''
Performance: P 3.11.2 (1769 ms, 43.83 Mb); P 3.9 PyPy 7.3.11 (568 ms, 65.95 Mb)
Time Complexity: O(N + M)
Auxiliary Space Complexity: O(N)
Test cases:
4 5
2 2
4 3
2 3
3 1
2 4
ans: 1 2 3 4
1 0
ans: 1
1 1
1 1
ans: 1
2 1
1 2
ans: 1
2 1
2 1
ans: 1 2
'''