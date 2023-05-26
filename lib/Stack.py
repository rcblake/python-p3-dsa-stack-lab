class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        return None if self.full() else self.items.append(item)

    def pop(self):
        return None if self.isEmpty() else self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items)==self.limit

    def search(self, target):
        if target in self.items:
            return self.size()-1 - self.items.index(target)
        else:
            return "-1"