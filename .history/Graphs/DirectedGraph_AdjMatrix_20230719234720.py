
# class Graph:
#     def __init__(self, numberOfNodes):
#         self.numberOfNodes = numberOfNodes +1
#         self.graph = [[0 for x in range(numberOfNodes+1)] for y in range(numberOfNodes+1)] #size of the matrix is number of nodes + 1 because of the 0 index
#     def withinBounds(self, v1, v2):
#         return (v1>=0 and v1 <= self.numberOfNodes) and (v2>=0 and v2<=self.numberOfNodes)

#     def insertEdge(self, v1, v2):
#         if (self.withinBounds(v1, v2)):
#             self.graph[v1][v2] = 1  #*means there is an edge from v1 to v2

#     def printGraph(self):
#         for i in range(self.numberOfNodes):
#             for j in range(len(self.graph[i])):
#                 if (self.graph[i][j]):
#                     print (i, "=> ", j)

# g = Graph(5)

# g.insertEdge(1,2)
# g.insertEdge(2,3)
# g.insertEdge(4,5)

# g.printGraph()

# class Graph:
#     def __init__(self, numberOfNodes):
#         self.numberOfNodes = numberOfNodes+1
#         self.graph = [[0 for x in range(self.numberOfNodes)] for y in range(self.numberOfNodes)]
    
#     def withinBounds(self,v1, v2):
#         return (v1>0 and v1<self.numberOfNodes) and (v2>0 and v2<self.numberOfNodes)
    
#     def insertEdge(self, v1, v2):
#         if self.withinBounds(v1,v2):
#             self.graph[v1][v2]=1
#         else:
#             print ("out of bounds")
#             return
    
#     def __str__(self):
#         mystr=""
#         for i in range(len(self.graph)):
#             for j in range(len(self.graph[i])):
#                 if self.graph[i][j]==1:
#                     mystr+= f"{i} => {j}\n"
#         return mystr





class Graph:
    def __init__(self,numberOfNodes):
        self.numberOfNodes=numberOfNodes+1
        self.graph = [[0 for x in range(self.numberOfNodes)] for y in range(self.numberOfNodes)]
    
    def withinBounds(self, v1, v2):
        return (v1>0 and v1<self.numberOfNodes) and (v2>0 and v2<self.numberOfNodes)
    def insertEdge(self, v1, v2):
        if self.withinBounds(v1, v2):
            self.graph[v1][v2]=1
    def __str__(self):
        my_str=""
        for i in range(self.numberOfNodes):
            for j in range(self.graph[i]):
                my_str+=f"{i} => {j}\n"
        return my_str



g = Graph(5)

g.insertEdge(1,2)
g.insertEdge(2,1)
g.insertEdge(6,4)
g.insertEdge(1,4)

print(g)
        