"""
Use DP for solution
Dynamics: min number of cubes needed to construct a number
Step: The new number can be seen as dp[i-cubes] as we can add exactly 1 cube to number i-cube and as we know
the min number of cubes for i-cube we can find such a cube from all available cubes that minimises the dynamics
"""
# read input
N = int(input())
# calculate cubes for first 100 natural numbers
cubes = []
for i in range(101):
    cubes.append(i**3)

dp = [_ for _ in range(N+1)]  # add extra 0, to keep indexation consistent

for i in range(2, len(cubes)):
    for j in range(cubes[i], N+1):
        dp[j] = min(dp[j-cubes[i]] + 1, dp[j])

print(dp[N])
'''
Complexity: O(n^(4/3))  # n^1/3 for iterating over cubes
Auxiliary Space: O(n)
Test cases:
1
ans: 1
27
ans: 1
9
ans: 2
33
ans: 5
35
ans: 2
'''