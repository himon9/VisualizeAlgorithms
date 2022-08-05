
from ast import Gt
import re
import sys
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self,v1,v2,wt):
        self.v1=v1
        self.v2=v2
        self.wt=wt
    def __str__(self):
        print(f"V1: {self.v1}")
        print(f"V2: {self.v2}")
        print(f"Wt: {self.wt}\n\n")

'''
vertexNo=int(input("Enter the total number of vertices : "))
edgeNo=int(input("Enter the total number of edges : "))


print("Enter the connection: Vertex1 Vertex2 Weight\n")
totalComp=[]
for i in range(edgeNo):
    print(f"\nEnter component {i}")
    objG= Graph(int(input("Enter v1: ")),int(input("Enter v2: ")),int(input("Enter wt: ")))
    totalComp.append(objG)
'''

#Example 1
totalComp=[
    Graph(0,1,4),Graph(0,7,8),Graph(1,2,8),Graph(1,7,11),Graph(2,3,7),
    Graph(2,8,2),Graph(2,5,4),Graph(3,4,9),Graph(3,5,14),Graph(4,5,10),
    Graph(5,6,2),Graph(6,8,6),Graph(6,7,1),Graph(7,8,7)
    ]
vertexNo=9
edgeNo=14
            
vertexSet=[range(vertexNo)]
#Printing the input graph
def draw(givenComp,graphName):
    edges=[[str(x.v1),str(x.v2)] for x in givenComp]
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    plt.figure()
    arc_rad=0.15
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in G.nodes()},
        connectionstyle=f'arc3, rad = {arc_rad}'
    )
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(str(x.v1),str(x.v2)):str(x.wt)   for x in givenComp},
        font_color='red'
    )
    plt.axis('off')
    plt.savefig(f"{graphName}.png", format="PNG")

draw(totalComp,"Input_Graph")

#Initialising dist and parent list
dist={x:sys.maxsize for x in range(vertexNo)}
startVertex=int(input("Enter the starting vertex : "))

dist[startVertex]=0
parent={x:-1 for x in range(vertexNo)}

storeGraph=totalComp

def extractMin():
    minVal=min(dist.values())
    for key,value in dist.items():
        if value==minVal:
            return key

def relax(objG,extractMinVertex):
    adjVertex=[]
    if objG.v1 != extractMinVertex:
        adjVertex=objG.v1
    else:
        adjVertex=objG.v2
    
    if dist[adjVertex]>dist[extractMinVertex]+objG.wt:
        dist[adjVertex]=dist[extractMinVertex]+objG.wt
        parent[adjVertex]=extractMinVertex

def adjVertex(currVertex):
    storeAdjComp=[]
    for obj in totalComp:
        adjVertex=[]
        if obj.v1==currVertex or obj.v2==currVertex:
            if obj.v1!=currVertex:
                adjVertex=obj.v1
            else:
                adjVertex=obj.v2

            if adjVertex in dist.keys():
                storeAdjComp.append(obj)
    return storeAdjComp

finalSet=[]
while dist:
    extractMinVertex=extractMin()
    finalSet.append(extractMinVertex)
    getAdjComps=adjVertex(extractMinVertex)    
    for objG in getAdjComps:
        relax(objG,extractMinVertex)
    del dist[extractMinVertex]


#print(f"Parent : {parent}\n")
endVertex=int(input("Enter the ending vertex : "))

reqPathComp=[]
def findPath(endVertex):
    while parent[endVertex]!=-1:
        for obj in totalComp:
            if obj.v1==endVertex and obj.v2==parent[endVertex]:
                reqPathComp.append(obj)
            elif obj.v1==parent[endVertex] and obj.v2==endVertex:
                reqPathComp.append(obj)
        endVertex=parent[endVertex]

findPath(endVertex)

#Drawing the shortest path from start to end vertex
draw(reqPathComp,"Shortest_Path")
