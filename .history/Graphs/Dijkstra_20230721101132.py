import heapq

# create a heap
H = [21,1,45,78,3,5]
heapq.heapify(H)
print("Heap : ", H)

# add elements to the heap
heapq.heappush(H,8)
print("Heap after push: ", H)

# remove element from the heap
print("Popped item : ", heapq.heappop(H))
print("Heap after pop: ", H)