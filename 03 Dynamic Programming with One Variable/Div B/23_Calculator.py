"""
Use DP for solution
Step: we may arrive to N by (N//3)*3 or (N//2)*2 or (N-1)+1, so compare the setups
ans(N) = min(ans(N-1)+1, #if N%2==0, ans(N//2) #if N%3==0. ans(N//3)
"""

# read input
N = int(input())

dp = [0, 0, 1, 1, 2]  # add extra 0 in the beginning to make indexing consistent, set up base case for 1,2,3,4
for i in range(5, N+1):
    if i%6 == 0:
        dp.append(min(dp[i//2]+1, dp[i//3]+1, dp[i-1]+1))
    elif i%3 == 0:
        dp.append(min(dp[i//3]+1, dp[i-1]+1))
    elif i%2 == 0:
        dp.append(min(dp[i//2]+1, dp[i-1]+1))
    else:
        dp.append(dp[i-1]+1)


# reconstruct the sequence
num = N
sequence = [num]
while num != 1:
    if num%6 == 0:
        min_temp = min(dp[num//2]+1, dp[num//3]+1, dp[num-1]+1)
        if min_temp == dp[num//2]+1:
                num //= 2
                sequence.append(num)
        elif min_temp == dp[num//3]+1:
                num //= 3
                sequence.append(num)
        elif min_temp == dp[num-1] + 1:
                num -= 1
                sequence.append(num)
    elif num%3 == 0:
        min_temp = min(dp[num // 3] + 1, dp[num - 1] + 1)
        if min_temp == dp[num // 3]+1:
                num //= 3
                sequence.append(num)
        elif min_temp == dp[num-1] + 1:
                num -= 1
                sequence.append(num)
    elif num%2 == 0:
        min_temp = min(dp[num // 2] + 1, dp[num - 1] + 1)
        if min_temp == dp[num // 2]+1:
                num //= 2
                sequence.append(num)
        elif min_temp == dp[num-1] + 1:
                num -= 1
                sequence.append(num)
    else:
        num -= 1
        sequence.append(num)

print(dp[N])
print(*sorted(sequence))  # print elements delimited by ' ', sorted to present in ascending order

'''
Complexity: O(N)
Auxiliary space: O(N)
Test cases:
1
ans: 0 1
5
ans: 3 1 3 4 5
2
ans: 1 1 2
'''


