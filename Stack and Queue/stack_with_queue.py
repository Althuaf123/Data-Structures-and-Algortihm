class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.current_size = 0

    def push(self, x):
        self.q1.append(x)
        self.current_size += 1

    def pop(self):
        if self.current_size == 0:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        popped = self.q1.pop(0)
        self.current_size -= 1
        self.q1, self.q2 = self.q2, self.q1
        return popped

    def size(self):
        return self.current_size

    def display(self):
        print(self.q1)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.display())
s.pop()
print(s.display())
s.pop()
print(s.display())
s.pop()
print(s.display())

