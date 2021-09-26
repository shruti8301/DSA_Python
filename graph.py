class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
c={"a": ["b","c"],
   "b": ["a","b","e"],
   "c": ["a","e"],
   "d": ["b","e","f"],
   "e": ["d","f"],
   "f": ["d","e"]}
   
graph=Graph(c)
graph.addEdge("e","c")
print(graph.gdict)
