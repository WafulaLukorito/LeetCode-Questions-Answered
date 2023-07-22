from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
    
    def bfs(self, startNode):
        visited = set()
        queue = deque()
        
        queue.append(startNode)
        visited.add(startNode)
        
        while(queue):
            cur = queue.popleft()
            print (cur, end=" ")
            
            for neighbor in self.graph[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
            




g = Graph()

g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.bfs(2)
