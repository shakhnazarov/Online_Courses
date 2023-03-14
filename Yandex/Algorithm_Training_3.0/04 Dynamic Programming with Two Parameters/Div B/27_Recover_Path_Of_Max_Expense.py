"""
Use DP
Dynamics: max possible expenditure to get from first cell to [i][j]
Step: choose max of the steps from above and from left
"""

# read input
N, M = map(int, input().split())
payments = [[0 for x in range(M+1)]]
for i in range(1, N+1):
    payments.append([0])
    payments[i].extend(list(map(int, input().split())))

# compute dynamics for all cells in the field
dp = [[-1 for x in range(M+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], 0) + payments[i][j]  # 0 to correctly set up base

# recover the answer
path = []
i = N
j = M
while i > 1 or j > 1:
    if dp[i][j] == dp[i-1][j] + payments[i][j]:
        path.append('D')
        i -= 1
    else:
        path.append('R')
        j -= 1

# print out the answer
print(dp[-1][-1])
print(*path[::-1])

'''
Performance: P 3.11.2 (988 ms, 5.94 Mb); P 3.9 PyPy 7.3.11 (687 ms, 40.25 Mb)
Complexity: O(N*M)
Auxiliary Space: O(N*M)
Test cases:
5 5
9 9 9 9 9
3 0 0 0 0
9 9 9 9 9
6 6 6 6 8
9 9 9 9 9
ans: 74 D D R R R R D D
1 1
1
ans: 1
1 3
1 2 3
ans: 6 R R
3 1
1
2
3
ans: 6 D D
2 2
1 2
3 4
ans: 8 D R
'''