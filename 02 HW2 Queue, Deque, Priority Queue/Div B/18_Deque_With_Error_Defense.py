class Deque:
    # constructor as in CPP
    def __init__(self):
        self.deque = []

    # what to represent when call "print()"
    def __str__(self):
        return f"{self.deque}"

    # add element to the beginning of deque
    def push_front(self, value):
        self.deque.insert(0, value)
        return "ok"

    # add element to the end of deque
    def push_back(self, value):
        self.deque.append(value)
        return "ok"

    # remove first element from deque
    def pop_front(self):
        if len(self.deque) != 0:
            return self.deque.pop(0)
        else:
            return "error"

    # remove last element from deque
    def pop_back(self):
        if len(self.deque) != 0:
            return self.deque.pop()
        else:
            return "error"

    # show first element of deque
    def front(self):
        if len(self.deque) != 0:
            return self.deque[0]
        else:
            return "error"

    # show last element of deque
    def back(self):
        if len(self.deque) != 0:
            return self.deque[-1]
        else:
            return "error"

    # show length of deque
    def size(self):
        return len(self.deque)

    # clear deque
    def clear(self):
        self.deque.clear()
        return "ok"


# create empty deque
deque = Deque()

# we know the stop word thus use infinite cycle
while True:
    # commands can be either 1 word or 2 words (if 1 word a list is still created(e.g. ["pop"])
    command = input().split()

    # switch was implemented in python 3.10
    match command[0]:
        case "push_back":
            print(deque.push_back(command[1]))
        case "push_front":
            print(deque.push_front(command[1]))
        case "pop_back":
            print(deque.pop_back())
        case "pop_front":
            print(deque.pop_front())
        case "back":
            print(deque.back())
        case "front":
            print(deque.front())
        case "size":
            print(deque.size())
        case "clear":
            print(deque.clear())
        case "exit":
            print("bye")
            break

'''
Test cases:
push_back 1
back
exit
ans: ok 1 bye
size
push_back 1
size
push_back 2
size
push_front 3
size
exit
ans: 0 ok 1 ok 2 ok 3 bye
push_back 3
push_front 14
size
clear
push_front 1
back
push_back 2
front
pop_back
size
pop_front
size
exit
ans: ok ok 2 ok ok 1 ok 1 2 1 1 0 bye
'''