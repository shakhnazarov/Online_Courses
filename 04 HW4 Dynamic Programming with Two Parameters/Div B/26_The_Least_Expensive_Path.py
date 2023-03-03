"""
Use DP to solve
DP: min value to pay to gen to the i,j point
Step: compare whether it is better to get to the point from above or from left
"""

# read input
N, M = map(int, input().split())
matrix = []  # NxM matrix
for i in range(N):
    matrix.append(list(map(int, input().split())))

# compute dynamic for each cell (it is faster to iterate by columns given a row)
dp = [[float('inf')] for x in range(N+1)]  # (N+1)x(M+1) matrix
dp[0] = [float('inf')]*(M+1)  # zero row and column by positive inf to set up a base
dp[0][1] = dp[1][0] = 0  # to correctly initialize starting cell
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i].append(matrix[i-1][j-1] + min(dp[i-1][j], dp[i][j-1]))

# answer
print(dp[-1][-1])

'''
Complexity: O(N*M)
Auxiliary Space: O(N*M)
Test cases:
1 1
2
ans: 2
2 2
1 2
1 2
ans: 4
5 5
1 1 1 1 1
3 100 100 100 100
1 1 1 1 1
2 2 2 2 1
1 1 1 1 1
ans: 11'''