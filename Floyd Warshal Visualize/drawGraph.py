import matplotlib.pyplot as plt
import networkx as nx
import my_draw_networkx_edge_labels as my_nx


def draw(edgeList,graphName):
    G = nx.DiGraph()
    edge_list=[(g.v1,g.v2,{'w':g.wt}) for g in edgeList]
    G.add_edges_from(edge_list)
    pos=nx.spring_layout(G,seed=5)
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    #fig.savefig("1.png", bbox_inches='tight',pad_inches=0)

    curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
    straight_edges = list(set(G.edges()) - set(curved_edges))
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
    arc_rad = 0.1
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')
    #fig.savefig("2.png", bbox_inches='tight',pad_inches=0)

    edge_weights = nx.get_edge_attributes(G,'w')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
    my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels,rotate=False,rad = arc_rad,font_size=8)
    nx.draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=straight_edge_labels,rotate=False,font_size=8)
    fig.savefig(f"{graphName}.png", bbox_inches='tight',pad_inches=0)