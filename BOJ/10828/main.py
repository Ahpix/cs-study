import sys

class Stack:
    def __init__(self):
        self.box = []

    def push(self, num):
        self.box.append(num)

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            a = self.top()
            self.box.pop()
            return a

    def size(self):
        return len(self.box)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.box[self.size()-1]
        
n = int(input())
cmd = ""
integer = 0

s = Stack()

for i in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd.startswith("push"):
        cmd, integer = cmd.split()
        integer = int(integer)
        s.push(integer)

    if cmd == "pop":
        print(s.pop())

    if cmd == "size":
        print(s.size())

    if cmd == "empty":
        print(1) if s.isEmpty() else print(0)

    if cmd == "top":
        print(s.top())
