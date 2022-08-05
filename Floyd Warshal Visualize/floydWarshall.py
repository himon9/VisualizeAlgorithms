import sys
import my_draw_networkx_edge_labels as my_nx
import matplotlib.pyplot as plt
import networkx as nx
import drawGraph

totV=int(input("Enter the total number of vertices : "))
totE=int(input("Enter the total number of edges : "))

class Graph:
    def __init__(self,v1,v2,wt):
        self.v1=v1
        self.v2=v2
        self.wt=wt
    def __str__(self):
        print(f"V1: {self.v1}")
        print(f"V2: {self.v2}")
        print(f"Wt: {self.wt}\n\n")


totalComp=[]

'''
print("Enter the directrd connection: Vertex1 Vertex2 Weight\n")
for i in range(totE):
    objG=Graph(int(input("\nEnter v1: ")),int(input("Enter v2: ")),int(input("Enter wt: ")))
    totalComp.append(objG)
'''
#totalComp=[Graph(0,1,3),Graph(0,3,5),Graph(1,0,2),Graph(1,3,4),Graph(2,1,1),Graph(3,2,2)]
totalComp=[
            Graph(1,0,4),Graph(2,1,8),Graph(0,2,3),Graph(2,0,3),Graph(4,1,2),Graph(1,3,1),
            Graph(3,1,1),Graph(2,3,2),Graph(2,4,6),Graph(4,2,6),Graph(4,2,6),Graph(3,4,4),
            Graph(4,3,4),Graph(1,4,2),Graph(4,1,1)
           ]
            

#Drawin the graph
drawGraph.draw(totalComp,"InputGraph")

D=[]
P=[i for i in range(totV) for j in range(totV)] #Storing in row major order

#Initialising matD[0]
D0=[]
for i in range(totV):
    store=[999]*totV
    store[i]=0
    for g in totalComp:
        if g.v1==i:
            store[g.v2]=g.wt
    D0.append(store)
D.append(D0)

for k in range(1,totV+1):
    rowD=[]
    for i in range(totV):
        colD=[0]*totV
        for j in range(totV):
            if D[k-1][i][j]>D[k-1][i][k-1]+D[k-1][k-1][j]:
                colD[j]=D[k-1][i][k-1]+D[k-1][k-1][j]
                P[i*totV+j]=P[(k-1)*totV+j]
            else:
                colD[j]=D[k-1][i][j]
        rowD.append(colD)
    D.append(rowD)

matP=[]
for i in range(totV):
    col=[]
    for j in range(totV):
        col.append(P[i*totV+j])
    matP.append(col)

#Now calculating the shortest path
startV=int(input("Enter the starting vertex : "))
destV=int(input("Enter the destination vertex : "))

path=[destV]
while startV!=destV:
    vertex=P[startV*totV+destV]
    path.append(vertex)
    destV=vertex
path.reverse()

print(f"Shortest Path : {path}\n")

def findWt(v1,v2):
    for obj in totalComp:
        if obj.v1==v1 and obj.v2==v2:
            return obj.wt
    return

pathComp=[]
for i in range(len(path)-1):
   g=Graph(path[i],path[i+1],findWt(path[i],path[i+1]))
   pathComp.append(g)

drawGraph.draw(pathComp,"Shorted_Pair_Path")
    
