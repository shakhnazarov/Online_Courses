"""
Use basic properties of arithmetic division and division with reminder
"""

# read input
N = int(input())  # number of students
K = int(input())  # number of assignments variants
row_petya = int(input())  # row of Petya's sit
column_petya = int(input())  # 1 if Petya sits to the right of the teacher (left to the Petya), 2 otherwise

place_petya = (row_petya - 1) * 2 + column_petya  # index of Petya's sit

ans = [0, 0]  # want to compare front and back sits [row, column]
if K + place_petya <= N:  # check if Vasya can sit behind Petya
    ans[0] = (K + place_petya + 1) // 2  # add 1 to be on the same row for odd and even numbers
    ans[1] = 2 if (K + place_petya) % 2 == 0 else 1  # inline if-statement
if place_petya - K >= 1:  # check if Vasya can sit in front of Petya
    # check whether front sit is nearer than back (note that it does not matter whether back place exists)
    if row_petya - ((place_petya - K + 1) // 2) < abs(ans[0] - row_petya):  # ans[0]==0 then row_petya > r_p - smt
        ans[0] = (place_petya - K + 1) // 2
        ans[1] = 2 if (place_petya - K) % 2 == 0 else 1


if ans[0] == 0:  # Vasya cannot get the same variant as Petya
    print(-1)
else:
    print(f"{ans[0]} {ans[1]}")

'''
Performance: P 3.11.2 (43 ms, 4.41 Mb); P 3.9 PyPy 7.3.11 (169 ms, 28.09 Mb)
Complexity: O(1)
Auxiliary Space Complexity: O(1)
Test Cases:
25
13
7
1
ans: -1
11
5
3
2
ans: 1 1
'''