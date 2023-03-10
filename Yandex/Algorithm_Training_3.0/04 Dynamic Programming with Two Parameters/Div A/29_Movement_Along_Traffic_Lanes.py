"""
Use DP
Dynamics: number of possible signs for i roads and j lines
"""
# read input
M, N = map(int, input().split())

dp = [[0 for _ in range(N+1)] for __ in range(M+1)]
dp[0][0] = 1
for i in range(1, M+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

print(dp[-1][-1])
'''
Complexity: O(M*N)
Auxiliary Space Complexity: O(N*M)
Test Cases:
4 2
ans: 7
2 1
ans: 1
'''