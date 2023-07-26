
from collections import defaultdict, deque

def num_flights(airports, routes, start):
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
    queue=deque(start)
    
    while queue:
        current_node = queue.popleft()
        for neighbor in current_node:
            if min_stops[current_node]+1 < min_stops[neighbor]:
                min_stops[neighbor] = min_stops[current_node]+1
                queue.append(neighbor)
    
    for key, value in min_stops:
        if value == float('infinity'):
            value = -1
    
    return min_stops