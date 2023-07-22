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
            
#             #*Process node only if current distance is less than the already calculated shortest distance
#             if current_distance <= distance[current_node]:
#                 for neighbor, weight in graph[current_node]:
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

class Solution:
    def networkDelayTime(self, times=[[2,1,1],[2,3,1],[3,4,1]], N=4, K=2):
        #*Initialize the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        #*create priority queue
        priority_queue=[(0,K)]
        
        #*Create a distance dictionary
        distance = {node: float("infinity") for node in range(1, N+1)}
        distance[K] = 0
        
        while priority_queue:
            current_distance, current_node = heapq.headpop(priority_queue)
            
            #*Process node if less than stored dict value
            if current_distance <= distance[current_node]:
                for neighbor, weight in graph[current_node]:
                    distance_to_neighbor = current_distance + weight
                    
                    #*If calculated distance < stored dist, update it and add neighbour to prority queue
                    if distance_to_neighbor < distance[neighbor]:
                        distance[neighbor] = distance_to_neighbor
                        heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))
                        
        max_distance = max(distance.values())
        return max_distance if max_distance < float("infinity") else -1


g = Solution()
print (g.networkDelayTime())