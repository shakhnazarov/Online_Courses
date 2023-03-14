"""
Find the differences between terms to find pattern, then define the base and recurrently a_n
"""

'''# Slow algorithm to find a_n = a_(n-1) + new_triangles
def triangles(iteration):
    new_triangles = 0
    for j in range(1, iteration+1):
        if iteration >= 2*j:
            new_triangles += 2*iteration-3*j + 2  # from certain point number of triangles of certain length grow by 2
        else:
            new_triangles += iteration - j + 1 # before number of triangles of certain length grow by 1

    return new_triangles
'''

# read input
N = int(input())
a = [0, 1, 5, 13]  # base
for i in range(4, N+1):
    a.append(1 + 3*a[i-1] - 3*a[i-2] + a[i-3] + (i+1)%2)  # +1 for even numbers

print(a[N])



'''# Find the 3 differences between the terms to find the pattern
dp = [0]
diff = [0, 0]
diff_2 = [0, 0, 0]
diff_3 = [0, 0, 0, 0]
for i in range(1, N+1):
    dp.append(dp[i-1] + triangles(i))
for i in range(2, N+1):
    diff.append(dp[i]-dp[i-1])
for i in range(3, N+1):
    diff_2.append(diff[i]-diff[i-1])
for i in range(4, N+1):
    diff_3.append(diff_2[i]-diff_2[i-1])

print(*dp)
print(*diff)
print(*diff_2)
print(*diff_3)
'''

'''
Performance: P 3.11.2 (104 ms, 7.83 Mb); P 3.9 PyPy 7.3.11 (168 ms, 28.10 Mb)
Complexity: O(N)
Auxiliary Space: O(N)  # can do O(1) if do not keep values except for 3 values of sequence
Test cases:
1
ans: 1
6
ans: 78
'''