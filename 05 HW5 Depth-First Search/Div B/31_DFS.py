"""
Use list of sets (set(vertexes)) to store the graph (set as multiple edges present) in adjacency list format
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, visited, now):
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            dfs(graph, visited, neigh)
    vertexes_comp.append(now)

# read input
N, M = map(int, input().split())
graph = [set() for x in range(N+1)]
visited = [False]*(N+1)
vertexes_comp = []  #global variable
for i in range(M):
    ver_1, ver_2 = map(int, input().split())
    if ver_1 == ver_2:  # exclude loops
        continue
    graph[ver_1].add(ver_2)
    graph[ver_2].add(ver_1)

# use dfs to find the component of first vertex
dfs(graph, visited, 1)
print(len(vertexes_comp))
print(*sorted(vertexes_comp))

'''
Complexity: O(NlogN+M)  #(N+M) for dfs and NlogN for sort
Auxiliary space complexity: O(N)  # if don't count recursion
Test cases:
4 5
2 2
3 4
2 3
1 3
2 4
ans: 4 1 2 3 4
1 1
1 1
ans: 1 1
2 3
1 1
1 2
2 2
ans: 2 1 2
'''



