"""
Just find loop using dfs
colors: 0 - white (have not been in the vertex), 1 - grey (been in the vertex) (we don't need 3 colors as graph is
undirected)
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, now, parent = None):
    global is_loop
    graph[now][0] = 1
    for neigh in graph[now][1]:
        if neigh == parent: # anything==None is False (except None)
            continue
        if graph[neigh][0] == 1 and not is_loop:  # add not is_loop to go only on the loop path and not check neighs
            is_loop = True
        if graph[neigh][0] == 0 and not is_loop:
            dfs(graph, neigh, now)
    if is_loop:
        loop.append(now)


# read input
N = int(input())
# convert from adjacency matrix to adjacency list
graph = [[0,[]] for i in range(N+1)]  # [[color, [neighbors]]]
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            graph[i][1].append(j+1)

loop = []  # global variable
global is_loop
is_loop = False
for i in range(1, N+1):
    if graph[i][0] == 1:  # if we have already been in component don't need to recheck
        continue
    dfs(graph, i)
    if is_loop:
        break

# print out the results
if is_loop:
    print("YES")
    print(len(loop))
    print(*loop)
else:
    print("NO")

'''
Complexity: O(N*M)  # on input, beside input O(N+M)
Auxiliary Space: O(N^2) # worst case for complete graph
Test cases:
3
0 1 1
1 0 1
1 1 0
ans: YES 3 3 2 1
4
0 0 1 0
0 0 0 1
1 0 0 0
0 1 0 0
ans: NO
5
0 1 0 0 0
1 0 0 0 0
0 0 0 1 1
0 0 1 0 1
0 0 1 1 0
ans: YES 3 5 4 3
1
0
ans: NO

'''