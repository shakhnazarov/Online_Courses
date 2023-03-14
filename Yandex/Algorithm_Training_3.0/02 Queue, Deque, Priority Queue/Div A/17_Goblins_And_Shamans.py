"""
Use two deques of +- equal length to quickly add to the middle of the goblins' queue. Want either to keep len of left
deque to be len(deque_r) or len(deque_r)-1 to add priority goblins in middle (for even length of queue) or just before
the middle (for odd length of queue)
"""
from collections import deque

# read input
N = int(input())
deque_l = deque()
deque_r = deque()
for i in range(N):
    command = input().split()
    if command[0] == '+':
        deque_l.appendleft(int(command[1]))
        if len(deque_l) - 1 == len(deque_r):  # if initially queue is odd
            deque_r.appendleft(deque_l.pop())
    if command[0] == '-':
        print(deque_r.pop())  # first command cannot be '-'
        if len(deque_l) - 1 == len(deque_r):
            deque_r.appendleft(deque_l.pop())
    if command[0] == '*':
        if len(deque_r) - 1 == len(deque_l):  # if initially queue is odd
            deque_l.append(int(command[1]))
        else:  # deques are of the same length
            deque_r.appendleft(int(command[1]))

'''
Performance: P 3.11.2 (504 ms, 6.76 Mb); P 3.9 PyPy 7.3.11 (597 ms, 29.29 Mb)
Complexity: O(N)
Auxiliary space: O(1)
Test cases:
2
+ 1
-
ans: 1
2
* 1
-
ans: 1
4
* 1
+ 2
-
-
ans: 1 2
7
+ 1
+ 2
-
+ 3
+ 4
-
-
ans: 1 2 3
10
+ 1
+ 2
* 3
-
+ 4
* 5
-
-
-
-
ans: 1 3 2 5 4
'''