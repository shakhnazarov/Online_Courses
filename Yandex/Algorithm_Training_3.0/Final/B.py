import heapq

# read input values
N, W = map(int, input().split())

tasks = []
for i in range(N):
    start, duration = map(int, input().split())
    tasks.append((start, start + duration, i+1))

# sort tasks by start time
tasks.sort()
ans = []
min_num = 0
# assign tasks to employees
heap = []
for task in tasks:
    if heap and heap[0][0] <= task[0]:
        # assign task to existing employee
        end_time, employee = heapq.heappop(heap)
        heapq.heappush(heap, (task[1], employee))
    else:
        # assign task to a new employee
        employee = len(heap) + 1
        min_num = max(min_num, len(heap)+1)
        heapq.heappush(heap, (task[1], employee))
    # save the employee number for each task
    tasks[task[2]-1] = (task[0], task[1], employee) # заменяем номер задачи на номер employee

# output the minimum number of employees
print(min_num)

# output the task order with the assigned employee number
for task in tasks:
    print(task[2], end=" ")