import time
"""
Use DP for solution
Step: The new number can be seen as either new exact cube (e.g. 27) or a sum of previous number (e.g. 32+1=33)
so. If num is exact cube, then it is an optimal ans, if it is the sum, we should dinf the minimum sum of dynamics
Base: calculate only for the first num
"""
# read input
N = int(input())
st = time.time()
# calculate cubes for first 100
cubes = set()
for i in range(1,101):
    cubes.add(i**3)

dp = [0]  # add extra 0, to keep indexation consistent
for i in range(1, N+1):
    if i in cubes:
        dp.append(1)
    else:
        min_temp = i  # always can construct number by summing up ones
        for j in range(1, i//2+1):  # for even check cases i = 2*(i//2) and for odd i = (i//2) + (i//2+1)
            if min_temp > dp[j] + dp[i-j]:
                min_temp = dp[j] + dp[i-j]
        dp.append(min_temp)

print(dp[N])
print(time.time() - st)
'''
Complexity: O(n^2)
Auxiliary Space: O(n)
Test cases:
1
ans: 1
27
ans: 1
9
ans: 2
33
ans: 5'''