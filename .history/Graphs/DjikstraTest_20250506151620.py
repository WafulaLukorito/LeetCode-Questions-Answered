
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


priority_queue = []

heapq.heappush(priority_queue, (2, "priority 2 task"))
heapq.heappush(priority_queue, (1, "priority 1 task"))
heapq.heappush(priority_queue, (3, "priority 3 task"))

while priority_queue:
    task = heapq.heappop(priority_queue)
    print(task)

print(priority_queue)


def dijkstra(graph, start):
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance <= distance[current_node]:
            for neighbor, weight in graph[current_node].items():
                distance_to_neighbor = current_distance + weight
                
                if distance_to_neighbor < distance[neighbor]:
                    distance[neighbor] = distance_to_neighbor
                    heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))
    
    return distance