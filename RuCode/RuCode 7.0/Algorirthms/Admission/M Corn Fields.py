
N = int(input())
rectangles = []
for i in range(N):
    rectangles.append(list(map(int, input().split())))

xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))  #retrieved all unique values of x1 and x2
x_i = {v: i for i, v in enumerate(xs)}  # dictionary (reversed key-value list)

count = [0] * len(x_i)
L = []
for x1, y1, x2, y2 in rectangles:
    L.append([y1, x1, x2, 1])
    L.append([y2, x1, x2, -1])
L.sort()

cur_y = cur_x_sum = area = 0

for y, x1, x2, sig in L:
    area += (y - cur_y) * cur_x_sum
    cur_y = y
    for i in range(x_i[x1], x_i[x2]):
        count[i] += sig
    cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
print(area % (10 ** 9 + 7))

# TL problem, perhaps 34 test case could be WA