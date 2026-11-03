# Queue Implementation

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, v):
        self.queue.append(v)
    def isempty(self):
        return (self.queue == [])
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    def __str__(self):
        return(str(self.queue))
    
# Queue implementation for adjacent list
def BFSList(AList, start_vertex):
    # Initialization
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False

    # Create a Queue object q
    q = Queue()

    # mark the first vertex as visited and insert it into the queue
    visited[start_vertex] = True
    q.enqueue(start_vertex)

    # Repeat the following untill queue is not empty
    while(not q.isempty()):
        # remove the one vertex from the queue
        curr_vertex = q.dequeue()
        # Visit the adjacent vertex of the the removed vertex if not visited, mark it as visited, add it to the queue
        for adj_vertex in AList[curr_vertex]:
            if(not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)
    return(visited)
AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSList(AList,0))






