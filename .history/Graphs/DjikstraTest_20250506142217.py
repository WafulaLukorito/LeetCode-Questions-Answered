
import heapq

H = [21,1,45,75,32,10,3]
heapq.heapify(H)
print("Heap : ", H)

heapq.heappush(H, 8)
heapq.heappush(H, 76)
heapq.heappush(H, 10)

print("heap after push: ", H)

print ("Popped item : ", heapq.heappop(H))
print ("Heap after pop : ", H)
print ("Popped item : ", heapq.heappop(H))
print ("Heap after pop : ", H)
print ("Popped item : ", heapq.heappop(H))
print ("Heap after pop : ", H)

priority_queue = []

heapq.heappush(priority_queue, (2, "priority 2 task"))
heapq.heappush(priority_queue, (1, "priority 1 task"))
heapq.heappush(priority_queue, (3, "priority 3 task"))

print(priority_queue)