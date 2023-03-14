"""
Use DP
Step: use min of the waiting time min(ans(N-1) + A_i, ans(N-2) + B_i_of_N-1, ans(N-3) + C_i_of_N-2) where ans(N) min
time for getting tickets for first N people (note that for last 2 people we do not consider whether they may bought
more tickets than needed for lesser time
Base: calculate times for the first 3 customers
"""
# read input (the task was solved in the lecture 3)
N = int(input())
customers = [[0,0,0]]  # [A_i, B_i, C_i]
for i in range(N):
    A_i, B_i, C_i = map(int, input().split())
    customers.append([A_i, B_i, C_i])

customers_wait = [0]  # first redundant zero to make indexation consistent
customers_wait.append(customers[1][0])
if N>1:
    customers_wait.append(min(customers[2][0] + customers[1][0], customers[1][1]))
    if N>2:
        customers_wait.append(min(
            customers[1][2],  # first bought for all
            customers_wait[2] + customers[3][0], # min buying for first two, 3rd bought themselves
            customers[1][0] + customers[2][1] # first bought themselves, 2nd bought for the 2nd and 3rd
        ))

for i in range(4, N+1):
    customers_wait.append(min(
        customers_wait[i-1] + customers[i][0],
        customers_wait[i-2] + customers[i-1][1],
        customers_wait[i-3] + customers[i-2][2]
    ))

print(customers_wait[N])

'''
Performance: P 3.11.2 (65 ms, 4.40 Mb); P 3.9 PyPy 7.3.11 (242 ms, 28.10 Mb)
Complexity: O(N)
Auxiliary Space: O(N)
Test cases:
5
5 10 15
2 10 15
5 5 5
20 20 1
20 1 1
ans: 12
1
3 2 1
ans: 1'''