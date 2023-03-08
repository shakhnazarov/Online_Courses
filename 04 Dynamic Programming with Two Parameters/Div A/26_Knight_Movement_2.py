"""
Use DP
Dynamics: number of ways to reach i,j cell
Step: add the number from i-2,j-1 and j-2, i-1 and i+1,j-2 and i-2, j+1 cells
"""

# read input
N, M = map(int, input().split())

dp_forward = [[0]*M for i in range(N)]
dp_forward[0][0] = 1  # can do nothing in exactly 1 way
for i in range(N):
    for j in range(M):
        if i - 2 >= 0 and j - 1 >= 0:  # check whether such cells even exist
            dp_forward[i][j] += dp_forward[i-2][j-1]
        if i - 1 >= 0 and j - 2 >= 0:
            dp_forward[i][j] += dp_forward[i-1][j-2]

dp_backward = [[0]*M for i in range(N)]
dp_backward[0][M-1] = 1  # can do nothing in exactly 1 way
for i in range(N):
    for j in range(M-1, -1, -1):
        if i - 1 >= 0 and j + 2 < M:
            dp_backward[i][j] += dp_backward[i - 1][j + 2]
        if i - 2 >= 0 and j + 1 < M:
            dp_backward[i][j] += dp_backward[i - 2][j + 1]

dp= [[0]*M for i in range(N)]
dp[0][0] = 1  # can do nothing in exactly 1 way
for i in range(N):
    for j in range(M):
        if i - 2 >= 0 and j - 1 >= 0:  # check whether such cells even exist
            dp[i][j] += dp[i-2][j-1]
        if i - 1 >= 0 and j - 2 >= 0:
            dp[i][j] += dp[i-1][j-2]
        if i + 1 < N and j - 2 >= 0:
            dp[i][j] += dp[i + 1][j - 2]
        if i - 2 >= 0 and j + 1 < M:
            dp[i][j] += dp[i - 2][j + 1]

print(dp[-1][-1])

'''
Complexity: O(N*M)
Auxiliary space: O(N*M)
Test cases:
1 1
ans: 1
3 2
ans: 1
2 2
ans: 0
31 34
ans: 293930
'''