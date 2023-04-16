n = int(input()) # number of orders
times = [] # list of tuples (time1, time2)
for i in range(n):
    t1, t2 = map(int, input().split())
    times.append((t1, t2))

# define memoization table to store the minimum time to complete all orders
# memo[i][j] represents the minimum time to complete the first i orders with the last order assigned to courier j
memo = [[float('inf')]*3 for i in range(n+1)]

# base case: no orders, so time to complete is 0 for both couriers
memo[0][1] = memo[0][2] = 0

# fill memo table using dynamic programming
for i in range(1, n+1):
    # option 1: assign order i to courier 1
    memo[i][1] = min(memo[i-1][1] + times[i-1][0], memo[i-1][2] + times[i-1][0] + times[i-1][1])
    # option 2: assign order i to courier 2
    memo[i][2] = min(memo[i-1][2] + times[i-1][0], memo[i-1][1] + times[i-1][0] + times[i-1][1])

# determine which courier to assign to each order
assignments = []
last_courier = 1 if memo[n][1] < memo[n][2] else 2
for i in range(n-1, -1, -1):
    if last_courier == 1:
        if memo[i][1] + times[i][0] <= memo[i][2] + times[i][0] + times[i][1]:
            assignments.append(1)
        else:
            assignments.append(2)
            last_courier = 2
    else: # last_courier == 2
        if memo[i][2] + times[i][0] <= memo[i][1] + times[i][0] + times[i][1]:
            assignments.append(2)
        else:
            assignments.append(1)
            last_courier = 1
assignments.reverse()

# output assignments
for a in assignments:
    print(a, end=' ')