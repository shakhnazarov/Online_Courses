"""
Use DP
Dynamics: number of ways to reach i,j cell
Step: add the number from i-2,j-1 and j-2, i-1 cells
"""

# read input
N, M = map(int, input().split())

dp = [[0]*M for i in range(N)]
dp[0][0] = 1  # can do nothing in exactly 1 way
for i in range(N):
    for j in range(M):
        if i - 2 >= 0 and j - 1 >= 0:  # check whether such cells even exist
            dp[i][j] += dp[i-2][j-1]
        if i - 1 >= 0 and j - 2 >= 0:
            dp[i][j] += dp[i-1][j-2]

print(dp[-1][-1])

'''
Performance: P 3.11.2 (988 ms, 5.94 Mb); P 3.9 PyPy 7.3.11 (687 ms, 40.25 Mb)
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