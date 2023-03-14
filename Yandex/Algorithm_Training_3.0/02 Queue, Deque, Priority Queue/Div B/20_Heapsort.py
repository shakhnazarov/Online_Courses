"""
An in-pace sort using priority queue
"""
class MaxHeap:
    def __init__(self, heap=None):
        if heap is None:
            heap = []
        self.heap = heap

        # MaxHeapify the inputted array
        # imperative to start from the middle of the heap (do not care about leaves) and go up
        # (otherwise won't srt properly (5 4 3 6 7 won't sort))
        for i in range((len(heap))//2, -1, -1):
            self.sift_down(i)

    def __str__(self):
        """Returns a string representation of the heap"""
        s = ''
        for elem in self.heap:
            s += str(elem) + ' '
        s = s[:len(s)-1]
        return s

    def insert(self, value):
        """
        Inserts the value into the heap
        """
        self.heap.append(int(value))
        self.sift_up()

    def extract(self):
        """
        Pops the maximum value from the heap
        """
        max_value = self.heap[0]  # store max value
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down()
        return max_value

    def sift_up(self):
        """
        Sifts up heap after adding a value to keep structure of heap
        """
        index = len(self.heap) - 1
        index_parent = (index - 1) // 2  # for index 'i' of a parent, children indexes
        while self.heap[index_parent] < self.heap[index]:  # works also for only root heap
            self.heap[index_parent], self.heap[index] = self.heap[index], self.heap[index_parent]
            index = index_parent
            index_parent = max((index - 1) // 2, 0)  # for 2-element heap index_parent becomes -1

    def sift_down(self, index_parent=0, end_len=None):
        """
        Sifts down heap after removing a value from the heap, also used in heapsort

        :param index_parent: choose form which index to sift down
        :param end_len: choose up to which element to keep heap consistent, mainly used for in-place heapsort
        """
        if end_len is None:
            end_len = len(self.heap)

        index_parent = index_parent
        while index_parent * 2 + 1 < end_len:  # check whether any children exist
            if 2 * index_parent + 2 == end_len:  # only one child
                max_index = 2 * index_parent + 1
            elif self.heap[2 * index_parent + 1] > self.heap[2 * index_parent + 2]:  # left child is greater
                max_index = 2 * index_parent + 1
            else:  # right child is greater or equal
                max_index = 2 * index_parent + 2

            if self.heap[index_parent] < self.heap[max_index]:  # swap only if child is greater than parent
                self.heap[index_parent], self.heap[max_index] = self.heap[max_index], self.heap[index_parent]
            index_parent = max_index  # update index

    def heap_sort(self):
        """In-place sort for the heap, note that heap structure is not preserved after sorting"""
        heap_size = len(self.heap)

        # for each iteration find the max value of the heap and preserve the heap structure
        for i in range(heap_size):
            self.heap[0], self.heap[heap_size-i-1] = self.heap[heap_size-i-1], self.heap[0]  # push max to the end
            self.sift_down(end_len=heap_size-i-1)
        return self.heap


# read input
N = int(input())
array = list(map(int, input().split()))

# sort in-place using MaxHeap
max_heap = MaxHeap(array)
print(*max_heap.heap_sort())

'''
Performance: P 3.11.2 (853 ms, 12.79 Mb); P 3.9 PyPy 7.3.11 (354 ms, 43.09 Mb)
Complexity (of sort): O(NlogN)
Auxiliary space: O(1)
Test cases:
1
1 12 9 5 6 10
ans: 1 5 6 9 10 12
1
1
ans: 1
2
3 1
ans: 1 3
'''