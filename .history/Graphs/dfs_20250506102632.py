


# from collections import defaultdict
# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)
    
#     def insertEdge(self, v1, v2):
#         self.graph[v1].append(v2)
        
#     def dfs(self, startNode):
#         visited=set()
#         st =[]
#         st.append(startNode)
        
#         while (len(st)):
#             cur = st[-1]
#             st.pop()
            
#             if (cur not in visited):
#                 print (cur, end=" -> ")
#                 visited.add(cur)
            
#             for node in self.graph[cur]:
#                 if node not in visited:
#                     st.append(node)

from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        
    def dfs(self, startNode):
        st=[]
        visited = set()
        
        st.append(startNode)
        
        while (len(st)):
            cur = st[-1]
            st.pop()
            
            if cur not in visited:
                print (cur, end=" => ")
                visited.add(cur)
            
            for node in reversed(self.graph[cur]):   # Reverse to maintain correct order
                if node not in visited:
                    st.append(node)
        
        
    
    def __str__(self):
        mystr= ""
        for node in self.graph:
            neighbors = ", ".join(str(val) for val in self.graph[node])
            mystr+=f"{node} => {neighbors}\n"
        return mystr
    
g = Graph()

g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

# print (g)

g.dfs(2)