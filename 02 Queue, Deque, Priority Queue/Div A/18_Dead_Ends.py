class MinHeap:
    def __init__(self, heap = None):
        if heap is None:
            heap = []  # will keep tuples (departure, dead end number)
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

    def pop(self):
        if len(self.heap) == 0:
            raise Exception("Don't pop an empty heap")
        else:
            min_value = self.heap[0]  # store max value
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.sift_down()
            return min_value

    def sift_up(self):
        index = len(self.heap) - 1
        parent_index = max((index-1)//2, 0)  # max only in case index = 0
        while self.heap[parent_index][0] > self.heap[index][0]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = max((index - 1) // 2, 0)

    def sift_down(self):
        index = 0
        left_child = 2*index + 1
        while left_child < len(self.heap):
            if left_child + 1 == len(self.heap):
                min_index = left_child
            elif self.heap[left_child][0] < self.heap[left_child+1][0]:
                min_index = left_child
            else:
                min_index = left_child + 1

            if self.heap[min_index][0] < self.heap[index][0]:
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            else:
                break
            index = min_index
            left_child = 2*index + 1



import heapq
# read input
K, N = map(int, input().split())
ans = []
de_heap = [i for i in range(1, K+1)]
departures_heap = MinHeap()
heapq.heapify(de_heap)
is_ok = True
broken_train = 0
ans = []

for i in range(1, N+1):
    arrival, departure = map(int, input().split())

    while len(departures_heap) != 0 and departures_heap[0][0] < arrival:
        dep_temp = departures_heap.pop()[1]
        heapq.heappush(de_heap, dep_temp)  # now this dead end is empty

    if len(de_heap) == 0: # assume that if all dead ends are occupied and train comes we cannot organize the schedule
        is_ok = False
        broken_train = i
        break
    else:
        de_temp = heapq.heappop(de_heap)  # the first available dead end
        # if train goes out we empty the dead end, several trains can go out simultaneously
        while len(departures_heap) != 0 and departures_heap[0][0] == arrival:
            dep_temp = departures_heap.pop()[1]
            heapq.heappush(de_heap, dep_temp)  # now this dead end is empty

    # train goes to dead end only after all necessary trains have departed
    departures_heap.add((departure, de_temp))
    ans.append(de_temp)

if is_ok:
    print(*ans)
else:
    print(f"{0} {broken_train}")



    