# read input
N = int(input())
carriages = list(map(int, input().split()))
carriages = carriages[::-1]  # it is easier to work with reverse list (pop function)

# use stack for the solution
stack = []  # dead end
A_way = [0]

for i in range(N):
    stack.append(carriages.pop())
    while len(stack) != 0 and stack[-1] == A_way[-1] + 1:
        A_way.append(stack.pop())

if len(stack) != 0:  # should have eliminated all carriages in stack in while cycle if can_be_ordered
    print("NO")
else:
    print("YES")


'''
Test cases:
1
1
Ans: YES
6
2 1 4 3 6 5
Ans: YES
6
3 2 1 6 5 4
Ans: YES
'''