import matplotlib.pyplot as plt
import networkx as nx

#Drawing the graph
def draw(givenEdgeSet,graphName):
    edges = [[str(x.v1),str(x.v2)] for x in givenEdgeSet]
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in G.nodes()}
    )
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(str(x.v1),str(x.v2)):str(x.wt) for x in givenEdgeSet},
        font_color='red'
    )
    plt.axis('off')
    plt.savefig(f"{graphName}.png", format="PNG")

class Graph:
    def __init__(self,v1,v2,wt,inc):
        self.v1=v1
        self.v2=v2
        self.wt=wt
        self.inc=inc
    def __str__(self):
        print(f"V1: {self.v1}")
        print(f"V2: {self.v2}")
        print(f"Wt: {self.wt}")
        print(f"Inc: {self.inc}\n")


totV=int(input("Enter the total number of vertices : "))
totE=int(input("Enter the total number of edges : "))

print("Enter the edge set\n")
edgeSet=[]
for i in range(totE):
    objG=Graph(int(input("\nEnter v1: ")),int(input("Enter v2: ")),int(input("Enter wt: ")),0)
    edgeSet.append(objG)

#Drawing the input graph
draw(edgeSet,"Input_Graph")

#sorted the edge set in non decreasing order
edgeSet=sorted(edgeSet, key=lambda x: x.wt)

def makeSet():
    vParent=[x for x in range(totV)]
    vRank=[0]*totV
    return (vParent,vRank)

vParent,vRank=makeSet()

def findSet(currVertex):
    parent=vParent[currVertex]
    while True:
        if(currVertex==parent):
            break
        currVertex=parent
        parent=vParent[currVertex]
        
    return currVertex

def rank(v):
    return vRank[v]

for i in range(totE):
    v1Parent=findSet(edgeSet[i].v1)
    v2Parent=findSet(edgeSet[i].v2)

    if v1Parent!=v2Parent:
        edgeSet[i].inc=1

        v1Rank=rank(edgeSet[i].v1)
        v2Rank=rank(edgeSet[i].v2)

        if v1Rank >= v2Rank :
            vRank[edgeSet[i].v1]+=1
            vRank[edgeSet[i].v2]+=1
            vParent[edgeSet[i].v2]=edgeSet[i].v1
        else:
            vRank[edgeSet[i].v1]+=1
            vRank[edgeSet[i].v2]+=1
            vParent[edgeSet[i].v1]=edgeSet[i].v2
    edgeSet[i].__str__()
    print(f"v1Parent : {v1Parent}, v2Parent : {v2Parent}\n")
    print(f"parent : {vParent}")
    print(f"Rank : {vRank}\n")
incEdges=[edge for edge in edgeSet if edge.inc == 1]
#Drawing the ouptut graph
draw(incEdges,"MST_graph")
print(vParent)
print(vRank)