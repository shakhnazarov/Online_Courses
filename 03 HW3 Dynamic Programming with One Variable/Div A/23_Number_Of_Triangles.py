"""
Use DP
Dynamics:
"""

# read input
N = int(input())

print(4**(N-1) + (4**(N-1)-1)//3)