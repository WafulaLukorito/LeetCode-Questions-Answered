
"""
    LeetCode #743
    https://leetcode.com/problems/network-delay-time/
    
    There are N network nodes, labelled 1 to N. Given times, a list of travel times as directed edges times[i] = (u, v, w), 
    where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target. 
    Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
    If it is impossible, return -1.
    
    Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
    Output: 2
    
    """
    
# from collections import defaultdict
# import heapq

# class Solution:
#     def networkDelayTime(self,  [[2,1,1],[2,3,1],[3,4,1]], N: int, K: int) -> int:
#         #*Create a graph
#         graph = defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((v,w))
        
#         #*Create a priority queue
#         priority_queue = [(0,K)]
        
#         #*Create a distance dictionary
#         distance = {node: float('infinity') for node in range(1, N+1)}
#         distance[K] = 0
        
#         while priority_queue:
#             current_distance, current_node = heapq.heappop(priority_queue)
            
#             #*Process node only if current distance is less than or equal the already calculated shortest distance
#             if current_distance <= distance[current_node]:
#                 for neighbor, weight in graph[current_node]:
                    # 
#                     distance_to_neighbor = current_distance + weight
                    
#                     #*If the calculated distance is less than the already known distance,
#                     #*update shortest distance and add neighbor to priority queue
#                     if distance_to_neighbor < distance[neighbor]:
#                         distance[neighbor] = distance_to_neighbor
#                         heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))
        
#         max_distance = max(distance.values())
#         return max_distance if max_distance < float('infinity') else -1

from collections import defaultdict
import heapq

def NetworkDelay(times, N, K):
    #Create graph
    graph = defaultdict(list)
    for gen_node, dest_node, time in times:
        graph[gen_node].append((dest_node, time))
        
    #Create priority queue
    priority_queue= [(0, K)]
    
    #Create dist map
    distance = {node: float('infinity') for node in range(1, N+1)}
    distance[K]=0
    
    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)
        
        #Process if current_time <= saved time
        if current_time <= distance[current_node]:
            for neighbor, time in graph[current_node]:
                total_time_to_neighbor = distance[current_node]+time
                
                #if total time from k to neghbor < saved time
                #add neighbor to priority queue
                if total_time_to_neighbor < distance[neighbor]:
                    distance[neighbor] = total_time_to_neighbor
                    heapq.heappush(priority_queue, (total_time_to_neighbor, neighbor))
                    
    max_dist = max(distance.values())
    return max_dist if max_dist < float('infinity') else -1



print (NetworkDelay([[2,1,1],[2,3,1],[3,4,1]], 4, 2))

def Network_delay(times, start_node, number_of_nodes):
    graph = defaultdict(list)
    for start, dest, time in times:
        graph[start]=[(dest, time)]
        
    #create min_heap
    min_heap=[(0,start_node)]
    
    #create time_dict
    time_dict={node: float('infinity') for node in range(1, number_of_nodes+1)}
    time_dict[start_node]=0
    
    while min_heap:
        current_node, current_time = heapq.heappop(min_heap)
        if current_time <= time_dict[current_node]:
            for neighbor, timetoneighbor in graph[current_node]:
                total_time_to_neighbor = current_time + timetoneighbor
                if total_time_to_neighbor < time_dict[neighbor]:
                    time_dict[neighbor]=total_time_to_neighbor
    
    max_time = max(time_dict.values())
    return max_time if max_time < float('infinity') else -1

print (Network_delay([[2,1,1],[2,3,1],[3,4,1]], 4, 2))