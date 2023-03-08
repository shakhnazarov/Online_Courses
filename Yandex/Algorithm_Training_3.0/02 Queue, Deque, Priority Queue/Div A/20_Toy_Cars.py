"""
Use greedy algorithm - remove the last needed car for the boy. To do this:
1) find all the moments when the car may be needed (basically index of the command)
2) modify heap such that it can retrieve the car which is least needed along with its index
"""
class MaxHeap:
    def __init__(self, heap = None):
        if heap is None:
            heap = []  # will keep tuples (next_encounter_time, toy_number)
        self.heap = heap

        for i in range(len(heap)//2, -1, -1):
            self.sift_down()

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, index):
        return self.heap[index]

    def add(self, pair):
        self.heap.append(pair)
        self.sift_up()

    def change_sign(self):
        # delete items from heap is too expensive, just store them with opposite sign, thus throw to the end of heap
        self.heap[0] = (-1*self.heap[0][0], self.heap[0][1])
        self.sift_down()

    def sift_up(self):
        index = len(self.heap) - 1
        parent_index = max((index-1)//2, 0)  # max only in case index = 0
        while self.heap[parent_index][0] < self.heap[index][0]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = max((index - 1) // 2, 0)

    def sift_down(self):
        index = 0
        left_child = 2*index + 1
        while left_child < len(self.heap):
            if left_child + 1 == len(self.heap):
                max_index = left_child
            elif self.heap[left_child][0] > self.heap[left_child+1][0]:
                max_index = left_child
            else:
                max_index = left_child + 1

            if self.heap[max_index][0] > self.heap[index][0]:
                self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            else:
                break
            index = max_index
            left_child = 2*index + 1


# read input
N, K, P = map(int, input().split())
orders = []
for i in range(P):
    orders.append(int(input()))

# will keep encounters for each element in descending order
order_next = [[P] for _ in range(N+1)]
for i in range(P-1, -1, -1):
    order_next[orders[i]].append(i)
for i in range(N+1):
    order_next[i].pop()  # as for each element added redundant entry

max_heap = MaxHeap()
on_floor = set()
count = 0
for order in orders:
    if order in on_floor:
        count -= 1  # if car is on the floor, mom won't do anything
    elif len(on_floor) == K:
        on_floor.remove(max_heap[0][1])  # delete the least needed car
        max_heap.change_sign()  #"delete" from heap - read .change_sign()
    max_heap.add((order_next[order].pop(), order))  # old pair will never be in maximum
    on_floor.add(order)
    count += 1

print(count)

'''
Complexity: O(NlogN)
Time complexity: O(N)
Test cases:
3 2 7
1
2
3
1
3
1
2
ans: 4
1 1 1
1
ans: 1
'''