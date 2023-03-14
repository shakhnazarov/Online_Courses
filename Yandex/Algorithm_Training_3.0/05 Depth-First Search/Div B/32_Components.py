"""
Use dfs in a loop for each vertex
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, now, visited):
    if not visited[now]:  # in the beginning to not double count vertexes
        component.append(now)
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            dfs(graph, neigh, visited)


# read input
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    ver_1, ver_2 = map(int, input().split())
    graph[ver_1].append(ver_2)  # add two times as graph is undirected
    graph[ver_2].append(ver_1)

# use dfs to find all components
components = []
component = [] # global variable
visited = [False for _ in graph]
for i in range(1, N+1):
    dfs(graph, i, visited)
    if len(component) > 0:  # len(component)==0 if visited the already found component
        components.append(component)
        component = []  # do not use .clear() or component[:] = [] as it will affect all values in components later

# print out the answer
print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)

'''
Performance: P 3.11.2 (394 ms, 23.43 Mb); P 3.9 PyPy 7.3.11 (397 ms, 47.17 Mb)
Time complexity: O(N+M)
Auxiliary space: O(N+M)
Test cases:
1 0
1
ans: 1 1 1
3 3
1 2
2 3
3 1
ans: 1 3 1 2 3
6 4
3 1
1 2
5 4
2 3
ans: 3 3 1 2 3 2 4 5 1 6
6 4
4 2
1 4
6 4
3 6
ans: 2 5 1 2 3 4 6 1 5 
0 0
ans: 0
'''
