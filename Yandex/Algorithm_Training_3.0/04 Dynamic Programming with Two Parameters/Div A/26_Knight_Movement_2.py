"""
Use forward DP and check cells on all possible secondary diagonals
Dynamics: number of ways to reach i,j cell
Step: add number to any reachable cell
"""

# read input
N, M = map(int, input().split())

dp= [[0]*M for i in range(N)]
dp[0][0] = 1  # can do nothing in exactly 1 way
for k in range(N+M-1):
    for i in range(k+1):
        j = k - i
        if i + 2 < N and j + 1 < M:  # check whether such cells even exist
            dp[i+2][j+1] += dp[i][j]
        if i + 1 < N and j + 2 < M:
            dp[i+1][j+2] += dp[i][j]
        if i - 1 >= 0 and j + 2 < M and i < N:
            dp[i-1][j+2] += dp[i][j]
        if i + 2 < N and j - 1 >= 0 and j < M:
            dp[i+2][j-1] += dp[i][j]

print(dp[-1][-1])

'''
Complexity: O((N+M)^2)
Auxiliary space: O(N*M)
Test cases:
1 1
ans: 1
2 3
ans: 1
4 4
ans: 2
'''