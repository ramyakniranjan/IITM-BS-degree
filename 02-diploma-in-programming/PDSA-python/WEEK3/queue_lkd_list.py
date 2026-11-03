class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        if self.front == None:
            return True
        else:
            return False

    def Enqueue(self, data):
        if self.isempty() == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            temp = Node(data)
            self.rear.next = temp
            self.rear = temp

    def Dequeue(self):
        if self.isempty() == True:
            return None
        elif self.front.next == None:
            temp = self.front.data
            self.front = None
            self.rear = None            
        else:
            temp = self.front.data
            self.front = self.front.next
        return temp

    def display(self):
        if self.isempty()==True:
            print(None)
        else:
            temp = self.front
            while temp != None:
                print(temp.data)
                temp = temp.next		


Q = Queue()
Q.Enqueue(30)
Q.Enqueue(40)
Q.Enqueue(50)
Q.Enqueue(60)
Q.Enqueue(70)
print(Q.Dequeue())
print(Q.Dequeue())
print(Q.Dequeue())
print(Q.Dequeue())
print(Q.Dequeue())
print(Q.Dequeue())
Q.display()
