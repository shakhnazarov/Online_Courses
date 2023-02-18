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