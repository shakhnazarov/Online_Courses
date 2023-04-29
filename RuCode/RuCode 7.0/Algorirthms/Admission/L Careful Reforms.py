n = int(input())

adj = [[] for i in range(n)]
for i in range(n):
    string = input()
    list_temp = []
    for s in string:
        list_temp.append(int(s))
    adj[i] = list_temp

# Create transitive closure matrix
tc = [[adj[i][j] for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            tc[i][j] = tc[i][j] or (tc[i][k] and tc[k][j])

# Print the transitive closure matrix
for i in range(n):
    for j in range(n):
        print(tc[i][j], end='')
    print()


# Python TL, c++ also TL