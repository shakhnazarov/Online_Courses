"""
Use DP
Dynamics:
"""
def triangles(iteration):
    new_triangles = 0
    for j in range(1, iteration+1):
        if iteration >= 2*j:
            new_triangles += 2*iteration-3*j + 2
        else:
            new_triangles += iteration - j + 1

    return new_triangles
# read input
N = int(input())

dp = [0]
for i in range(1, N+1):
    dp.append(dp[i-1] + triangles(i))

print(dp[-1])