"""
Just find cycle using dfs
colors: 0 - white (have not been in the vertex), 1 - grey (been in the vertex) (we don't need 3 colors as graph is
undirected)
"""
import sys
sys.setrecursionlimit(100001)  # initial limit is usually 1000

def dfs(graph, now, parent = None):
    global is_cycle, is_finished, start_cycle
    graph[now][0] = 1
    for neigh in graph[now][1]:
        if neigh == parent: # anything==None is False (except None)
            continue
        if graph[neigh][0] == 1 and not is_cycle:  # add not is_cycle to go only on the cycle path and not check neighs
            is_cycle = True
            is_finished = False
            start_cycle = neigh
            cycle.append(start_cycle)
        if graph[neigh][0] == 0 and not is_cycle:
            dfs(graph, neigh, now)
    if is_cycle and not is_finished:
        if now == start_cycle:
            is_finished = True
        else:
            cycle.append(now)


# read input
N = int(input())
# convert from adjacency matrix to adjacency list
graph = [[0,[]] for i in range(N+1)]  # [[color, [neighbors]]]
for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            graph[i][1].append(j+1)

cycle = []  # global variable
global is_cycle
is_cycle = False
for i in range(1, N+1):
    if graph[i][0] == 1:  # if we have already been in component don't need to recheck
        continue
    dfs(graph, i)
    if is_cycle:
        break

# print out the results
if is_cycle:
    print("YES")
    print(len(cycle))
    print(*cycle)
else:
    print("NO")

'''
Complexity: O(N*M)  # on input, beside input O(N+M)
Auxiliary Space: O(N+M)
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