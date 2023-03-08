class Stack:
    # constructor as in CPP
    def __init__(self):
        self.stack = []

    # what to represent when call "print()"
    def __str__(self):
        return f"{self.stack}"

    # add element to stack
    def push(self, value):
        self.stack.append(value)
        return "ok"

    # remove last element from stack
    def pop(self):
        try:
            return self.stack.pop()
        except:
            return "error"

    # show last element of stack
    def back(self):
        try:
            return self.stack[-1]
        except:
            return "error"

    # show length of stack
    def size(self):
        return len(self.stack)

    # clear stack
    def clear(self):
        self.stack.clear()
        return "ok"


# create empty stack
stack = Stack()

# we know the stop word thus use infinite cycle
while True:
    # commands can be either 1 word or 2 words (if 1 word list is still created)
    command = input().split()

    # switch was implemented in python 3.10
    match command[0]:
        case "push":
            print(stack.push(command[1]))
        case "pop":
            print(stack.pop())
        case "back":
            print(stack.back())
        case "size":
            print(stack.size())
        case "clear":
            print(stack.clear())
        case "exit":
            print("bye")
            break
