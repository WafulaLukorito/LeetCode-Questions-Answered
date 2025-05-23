


class Graph:
    def __init__(self, numberOfNodes):
        self.numberOfNodes = numberOfNodes +1
        self.graph = [[0 for x in range(numberOfNodes+1)] for y in range(numberOfNodes+1)] #size of the matrix is number of nodes + 1 because of the 0 index
    def withinBounds(self, v1, v2):
        return (v1>=0 and v1 <= self.numberOfNodes) and (v2>=0 and v2<=self.numberOfNodes)

    def insertEdge(self, v1, v2):
        if (self.withinBounds(v1, v2)):
            self.graph[v1][v2] = 1  #*means there is an edge from v1 to v2
            self.graph[v2][v1] = 1 

    def printGraph(self):
        for i in range(self.numberOfNodes):
            for j in range(len(self.graph[i])):
                if (self.graph[i][j]):
                    print (i, "=> ", j)

g = Graph(5)

g.insertEdge(1,2)
g.insertEdge(2,3)
g.insertEdge(4,5)

g.printGraph()