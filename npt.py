import networkx as nx
G = nx.Graph()
G = nx.read_edgelist("npt.edgelist", nodetype=int)
G = nx.Graph(((u, v, e) for u,v,e in G.edges(data=True) if e['capacity'] == 1))

print("shortest paths")
for (u,v,e) in G.edges(data=True):
    print(nx.shortest_path(G, u, v, weight='distance'))

for (u,v,e) in G.edges(data=True):
    print("simple paths %d to %d" % (u, v))
    for path in nx.all_simple_paths(G, source=u, target=v):
        print(path)
