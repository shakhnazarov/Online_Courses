"""
Topological sort - naming of vertexes in such way that no vertex receives and edge from a vertex of higher number-name
Use dfs to find the order
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, visited, now):
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            dfs(graph, visited, neigh)

# read input
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    ver_1, ver_2 = map(int, input().split())
    graph[ver_1].append(ver_2)  # add one time as graph is oriented
