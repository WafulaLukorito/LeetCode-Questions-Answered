    """
    Array based implementation of a queue
    """
    
class Queue:
    def __init(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item) # O(1)
    
    def is_empty(self):
        return self.queue == [] # O(1)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) # O(n)
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)
    
class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return self.queue ==[]
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def deque(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)

#     """Linked list implementation of a queue
#     """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next
        self.count += 1
    
    def dequeue(self):
        if self.head is None:
            return None
        else:
            item = self.head.data
            self.head = self.head.next
            self.count -= 1
            return item
    