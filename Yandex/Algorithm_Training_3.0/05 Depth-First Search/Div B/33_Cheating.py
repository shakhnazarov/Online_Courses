"""
Basically, need to find bipartite graph. Do this by using dfs and colorize the vertexes in two colors, if neighbor
is of the same color then graph is not bipartite
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, now, visited, color):
    if not visited[now]:  # in the beginning to not double count vertexes
        visited[now] = True
        # colorize vertex
        if color == 1:
            graph[now][0] = 1
            color = 2
        else:
            graph[now][0] = 2
            color = 1
        for neigh in graph[now][1]:
            if graph[neigh][0] == graph[now][0]:
                global is_bipartite  # cannot initialize just declare global variable
                is_bipartite = False
            if not visited[neigh]:
                dfs(graph, neigh, visited, color)

# read input
N, M = map(int, input().split())
graph = [[0, []] for i in range(N+1)]  # [[color, [neighbors]]]
for i in range(M):
    ver_1, ver_2 = map(int, input().split())
    graph[ver_1][1].append(ver_2)  # add two times as graph is undirected
    graph[ver_2][1].append(ver_1)

# use dfs to colorize graph
visited = [False for _ in graph]
is_bipartite = True  # global variable
color = 1
for i in range(1, N+1):
    dfs(graph, i, visited, color)

if is_bipartite:
    print("YES")
else:
    print("NO")

'''
Time complexity: O(N+M)
Auxiliary space: O(N+M)
Test cases:
1 0
1
ans: YES
3 3
1 2
2 3
1 3
ans: NO
3 2
1 2
2 3
ans: YES
2 1
1 2
ans: YES
3 1
1 2
ans: YES
'''