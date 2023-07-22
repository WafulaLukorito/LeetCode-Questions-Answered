
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
    
    def __str__(self):
        mystr= ""
        for i in range (len(self.graph)):
            neighbors = ", ".join(str(val) for val in self.graph[i])
            mystr+=f"{self.graph[i]} => {neighbors}"
        return mystr
    
g = Graph()

g.insertEdge(2,5)
g.insertEdge(2,6)
g.insertEdge(4,5)

print (g)