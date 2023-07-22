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
    
    
    
import heapq

def dijkstra(graph, start):
    # Distance dictionary will store shortest distance from start to each node
    distance = {node: float('infinity') for node in graph}
    distance[start] = 0

    # Priority queue to select node with smallest distance
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Process node only if current distance is less than the already calculated shortest distance
        if current_distance <= distance[current_node]:
            for neighbor, weight in graph[current_node].items():
                distance_to_neighbor = current_distance + weight

                # If the calculated distance is less than the already known distance,
                # update shortest distance and add neighbor to priority queue
                if distance_to_neighbor < distance[neighbor]:
                    distance[neighbor] = distance_to_neighbor
                    heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

    return distance


# Test with a graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1},
}
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
