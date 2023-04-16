n = int(input())
train = []
count = {}

for _ in range(n):
    operation = input().split()

    if operation[0] == "add":
        num_wagons, goods = int(operation[1]), operation[2]
        train.append((goods, num_wagons))
        count[goods] = count.get(goods, 0) + num_wagons

    elif operation[0] == "delete":
        num_wagons = int(operation[1])
        while num_wagons > 0:
            while train[-1][1] == 0:
                train.pop()
            if train[-1][1] >= num_wagons:
                train[-1] = (train[-1][0], train[-1][1] - num_wagons)
                count[train[-1][0]] -= num_wagons
                break
            else:
                num_wagons -= train[-1][1]
                count[train[-1][0]] -= train[-1][1]
                train.pop()
    elif operation[0] == "get":
        goods = operation[1]
        print(count.get(goods, 0))