
from collections import defaultdict, deque

def num_flights(airports, routes, start):
    
    airports = set()
    for route in routes:
        airports.add(route[0])
        airports.add(route[1])
    
    if start not in airports or end not in airports:
        return -1
    #Create graph
    graph = defaultdict(list)
    for airport in airports:
        graph[airport]= []
    
    #populate graph
    for route in routes:
        graph[route[0]].append(route[1])
        
    
    #Create dict to track minimum distances
    min_stops= {airport: float('infinity') for airport in airports}
    min_stops[start]=0
    
    #create queue to keep track
    queue=deque([start])
    
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if min_stops[current_node]+1 < min_stops[neighbor]:
                min_stops[neighbor] = min_stops[current_node]+1
                queue.append(neighbor)
    
    for key, value in min_stops.items():
        if value == float('infinity'):
            min_stops[key] = -1
    
    return min_stops




#* Dijkistra implementation?

import heapq

def num_flights(airports, routes, start):
    # Create graph
    graph = defaultdict(list)
    for airport in airports:
        graph[airport]= []
    
    # Populate graph
    for route in routes:
        graph[route[0]].append(route[1])
    
    # Create dict to track minimum distances
    min_stops = {airport: float('infinity') for airport in airports}
    min_stops[start] = 0
    
    # Create priority queue to keep track, initialized with the starting node
    queue = [(0, start)]
    
    while queue:
        # Pop the airport with the smallest distance
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > min_stops[current_node]:
            continue
        
        # Iterate over neighbors in the graph
        for neighbor in graph[current_node]:
            distance = current_distance + 1
            if distance < min_stops[neighbor]:
                min_stops[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    # Change float('infinity') to -1 for unreachable airports
    for airport, distance in min_stops.items():
        if distance == float('infinity'):
            min_stops[airport] = -1
            
    return min_stops
