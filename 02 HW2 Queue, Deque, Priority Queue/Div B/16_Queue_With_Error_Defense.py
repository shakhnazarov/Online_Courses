class Queue:
    # constructor as in CPP
    def __init__(self):
        self.queue = []

    # what to represent when call "print()"
    def __str__(self):
        return f"{self.queue}"

    # add element to queue (to the end)
    def push(self, value):
        self.queue.append(value)
        return "ok"

    # remove first element from queue
    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
        else:
            return "error"

    # show first element of queue
    def front(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return "error"

    # show length of queue
    def size(self):
        return len(self.queue)

    # clear queue
    def clear(self):
        self.queue.clear()
        return "ok"


# create empty queue
queue = Queue()

# we know the stop word thus use infinite cycle
while True:
    # commands can be either 1 word or 2 words (if 1 word a list is still created(e.g. ["pop"])
    command = input().split()

    # switch was implemented in python 3.10
    match command[0]:
        case "push":
            print(queue.push(command[1]))
        case "pop":
            print(queue.pop())
        case "front":
            print(queue.front())
        case "size":
            print(queue.size())
        case "clear":
            print(queue.clear())
        case "exit":
            print("bye")
            break

'''
Test cases:
push 1
front
exit
ans: ok 1 bye
size
push 1
size
push 2
size
push 3
size
exit
ans: 0 ok 1 ok 2 ok 3 bye
push 3
push 14
size
clear
push 1
front
push 2
front
pop
size
pop
size
exit
ans: ok ok 2 ok ok 1 ok 1 1 1 2 0 bye
'''