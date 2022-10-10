import networkx as nx
G = nx.Graph()
G = nx.read_edgelist("npt.edgelist", nodetype=int)
G = nx.Graph(((u, v, e) for u,v,e in G.edges(data=True) if e['capacity'] == 1))
print(nx.shortest_path(G, 1, 5))