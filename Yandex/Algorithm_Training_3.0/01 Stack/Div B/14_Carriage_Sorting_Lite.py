"""
use stack to keep part of the carriages
"""
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
Performance: P 3.11.2 (50 ms, 4.41 Mb); P 3.9 PyPy 7.3.11 (177 ms, 28.32 Mb)
Complexity: O(N)
Auxiliary Space: O(N)
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