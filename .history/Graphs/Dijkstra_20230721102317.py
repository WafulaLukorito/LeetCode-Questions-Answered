import heapq

# create a heap
H = [21,1,45,78,3,5]
heapq.heapify(H)
print("Heap : ", H)

# add elements to the heap
heapq.heappush(H,8)
heapq.heappush(H,10)
heapq.heappush(H,18)
print("Heap after push: ", H)

# remove element from the heap
print("Popped item : ", heapq.heappop(H))
print("Heap after pop: ", H)



# create a priority queue
priority_queue = []

# add elements to the queue (with priorities)
heapq.heappush(priority_queue, (2, 'priority 2 task'))
heapq.heappush(priority_queue, (1, 'priority 1 task'))
heapq.heappush(priority_queue, (3, 'priority 3 task'))

while priority_queue:
    # remove and return the lowest priority task
    task = heapq.heappop(priority_queue)
    print(task)