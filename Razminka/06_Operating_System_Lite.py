# read input
M = int(input())
N = int(input())

# placeholder list of len M
placeholder = [False]*M

# create counter for available systems
counter = 0

# intersect the new system with the old
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, y-x+1):
        if placeholder[j] is True: # можно наткнуться как на одну систему так и на несколько,непонятно что делать
            counter -= 1
        else:
            placeholder[j] = True
    counter += 1
