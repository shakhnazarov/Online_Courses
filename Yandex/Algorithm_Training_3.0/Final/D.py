import math

# read input values
x_l, x_r = map(int, input().split())
r = int(input())
n = int(input())

# determine the maximum diameter of the bed
max_diameter = 0
for i in range(n):
    x, y = map(int, input().split())
    # check if the bed can fit between the tree and the walls
    if (y <= r and x_l + r > x - math.sqrt(r**2 - y**2)) or \
            (y <= r and x_r - r < x + math.sqrt(r**2 - y**2)):
        # calculate the diameter of the bed that can fit
        diameter = 2 * math.sqrt(r**2 - y**2)
        if diameter > max_diameter:
            max_diameter = diameter

# print the maximum diameter of the bed
print('{:.3f}'.format(max_diameter))