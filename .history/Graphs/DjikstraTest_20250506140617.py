
import heapq

H = [21,1,45,75,32,10,3]
heapq.heapify(H)
print("Heap : ", H)

heapq.heappush(H, 8)
heapq.heappush(H, 76)
heapq.heappush(H, 10)

print("heap after push: ", H)