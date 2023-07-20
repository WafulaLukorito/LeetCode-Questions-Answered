    
"""IMPLEMENT DIRECTED GRAPH USING AN ADJACENCY LIST
    """

# from collections import defaultdict


# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list) #*Points to a list of values that correspond to a node
    
#     def insertEdge(self, v1, v2): #*create relations b2n edges
#         self.graph[v1].append([v2])

#     def printGraph(self):
#         for node in self.graph:
#             for v in self.graph[node]:
#                 print(node, "=>", v)


# my_graph = Graph()

# my_graph.insertEdge(1,5)
# my_graph.insertEdge(5,2)
# my_graph.insertEdge(2,7)
# my_graph.insertEdge(7,1)

# my_graph.printGraph()



# from collections import defaultdict


# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def insertEdge(self, v1, v2):
#         self.graph[v1].append([v2])
    
#     def printGraph (self):
#         for node in self.graph:
#             for val in self.graph[node]:
#                 print(node, "=>", val)

# myGraph = Graph()
# myGraph.insertEdge(1,8)
# myGraph.insertEdge (8,9)
# myGraph.insertEdge(9, 3)
# myGraph.insertEdge(3, 7)

# myGraph.printGraph()



# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
        
#     def insertEdge(self, v1, v2):
#         self.graph[v1].append(v2)
    
#     def __str__(self):
#         output = ""
#         for node in self.graph:
#             neighbors = ", ".join(str(val) for val in self.graph[node])
#             output += f"{node} => {neighbors}\n"
#         return output.rstrip()

# myGraph = Graph()

# myGraph.insertEdge(1,8)
# myGraph.insertEdge (8,9)
# myGraph.insertEdge(9, 3)
# myGraph.insertEdge(3, 7)

# print(myGraph)

# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph= defaultdict(list)
#     def insertEdge(self, v1, v2):
#         self.graph[v1].append(v2)
#     def __str__(self):
#         output = ""
#         for node in self.graph:
#             print (str(node))
#             neighbors = ", ".join(str(val) for val in self.graph[node])
#             output += f"{node} => {neighbors}\n"
#         return output.rstrip()

# myGraph = Graph()

# myGraph.insertEdge(1,8)
# myGraph.insertEdge (8,9)
# myGraph.insertEdge(9, 3)
# myGraph.insertEdge(3, 7)

# print(myGraph)

from collections import defaultdict

class Graph2:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def insertEdge(self, v1, v2,):
        self.graph[v1].append(v2)
    
    def __str__(self):
        output= ""
        for node in self.graph:
            neighbours = ", ".join(str(val) for val in self.graph[node])
            output += f"{node} => {neighbours}"
            return output.rstrip()

myGraph2 = Graph2()

myGraph2.insertEdge(1,2)
myGraph2.insertEdge(1,3)
myGraph2.insertEdge(2,7)
myGraph2.insertEdge(3, 7)

print(myGraph2)