"""
Use properties of the Euclidean coordinate system
"""
# read input
n = int(input())
x_arr = []
y_arr = []
for i in range(n):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

# the minimal rectangle converge __just enough__
print(min(x_arr), min(y_arr), max(x_arr), max(y_arr))

'''
Performance: P 3.11.2 (46 ms, 4.39 Mb); P 3.9 PyPy 7.3.11 (574 ms, 28.31 Mb)
Complexity: O(1)
Auxiliary Space: O(1)
Test cases:
3
1 1
1 10
5 5
ans: 1 1 5 10
'''