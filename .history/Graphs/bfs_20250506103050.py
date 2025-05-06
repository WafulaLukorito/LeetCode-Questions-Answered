# from collections import defaultdict, deque

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     def insertEdge(self, v1, v2):
#         self.graph[v1].append(v2)
    
#     def bfs(self, startNode):
#         visited = set()
#         q = deque()
#         q.append(StartNode)
#         visited.append(StartNode)
        
#         while q:
#             cur = q.popleft()
#             print (cur, end= " ")
            
#             for neighbor in self.graph[cur]:
#                 if neighbor not in visited:
#                     q.append(neighbor)
#                     visited.add(neighbor)

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
    
    def bfs(self, startNode):
        q = deque()
        visited = set()
        
        q.append(startNode)
        visited.add(startNode)
        
        while q:
            cur = q.popleft()
            print (cur, end=" -> ")
            
            for node in self.graph[cur]:
                if node not in visited:
                    q.append(node)
                    visited.add(node)
                    


g = Graph()

g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.bfs(2)
