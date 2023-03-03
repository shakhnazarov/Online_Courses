"""
Use DP for solution
Dynamics 1: number of money spent
Dynamics 2: number of coupons
Step: If we had all possible coupons check in what min value way we could get to the day i (if price[i] > 100 then we
either spend coupon or spend money and gained coupon, if price <= 100 then we either spend coupon or just paid money)
"""

# read input
N = int(input())
prices = [0]  # false zero for easier indexation
for i in range(N):
    prices.append(int(input()))

# note that if we want to find the min we simulate the non-achievable outcomes with positive infinity
dp = [[float('inf')]*(N+3) for i in range(N+1)]  # [accumulated payment] second index is (the number of coupons - 1)
dp[0][1] = 0  # to drive the initial case
for i in range(1, N+1):  # days
    for j in range(1, N+2):  # coupons
        if prices[i] <= 100:
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j] + prices[i])  # as N+3 length we can check even for N+2'th coupon
        else:
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j-1] + prices[i])

# find the optimal value
min_value = float('inf')
min_index = -1
for i in range(1, N+2):  # iterate over coupons in the last day
    if min_value >= dp[-1][i]:  # the more coupons the better given the same expenditure
        min_value = dp[-1][i]
        min_index = i

# recover the answer
ans = []
j = min_index
for i in range(N, 0, -1):
    if prices[i] <= 100:
        if dp[i][j] == dp[i-1][j+1]:
            ans.append(i)
            j += 1
    elif dp[i][j] == dp[i-1][j+1]:
        ans.append(i)
        j += 1
    else:
        j -= 1

# print out the answer
print(min_value)
print(f"{min_index-1} {len(ans)}")
print(*ans[::-1])
