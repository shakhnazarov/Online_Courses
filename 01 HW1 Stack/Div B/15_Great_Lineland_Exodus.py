# read input
N = int(input())
avg_prices = list(map(int, input().split()))

# similar to the task "Поиск ближайшего меньшего справа"
stack = [[-1, -1]]  # [[price, index]], initialize with value to use [-1] indexing later for first element
ans = [-1] * N  # if lower price was not found for the city, ans is "-1"
for i, price in enumerate(avg_prices):
    while price < stack[-1][0]:  # check if price in current city is lower than for the city with lowers price in stack
        ans[stack.pop()[1]] = i
    stack.append([price, i])  # note that stack will always be in the non-increasing order

# print out the list with " " as delimiters
for elem in ans:
    print(elem, end=' ')  # note that it won't matter if we print out last " ", system will accept

'''
test cases:
2
0 0 
ans: -1 -1
3
2 1 0
ans: 1 2 -1
3
0 1 2
ans: -1 -1 -1
'''
