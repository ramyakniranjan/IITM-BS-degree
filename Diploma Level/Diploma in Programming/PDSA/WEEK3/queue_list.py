class Queue:
    def __init__(self):
        self.queue = []
    def isempty(self):
        return(self.queue == [])
    def enqueue(self, v):
        self.queue.append(v)
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    def __str__(self):
        return(str(self.queue))
    
Q = Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(40)
Q.enqueue(15)
print(Q.dequeue())
print(Q.dequeue())    