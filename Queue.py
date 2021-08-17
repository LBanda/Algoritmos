class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def Add(self,item):
        self.stack1.append(item)
    def Remove(self):
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

r = Queue()
r.Add(1)
r.Add(15)
r.Add(9)
r.Add(99)
r.Add(77)
r.Remove()
