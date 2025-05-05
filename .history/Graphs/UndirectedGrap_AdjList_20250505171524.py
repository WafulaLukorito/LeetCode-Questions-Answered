from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append (v1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    def printGraph (self):
        for node in self.graph:
            for val in self.graph[node]:
                print(node, "=>", val)

myGraph = Graph()
myGraph.insertEdge(1,8)
myGraph.insertEdge (1,9)
myGraph.insertEdge(9, 3)
myGraph.insertEdge(3, 7)

myGraph.printGraph()