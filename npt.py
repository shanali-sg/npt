# import networkx modules
import networkx as nx
G = nx.Graph()

# read edgelist from a file
G = nx.read_edgelist("npt.edgelist", nodetype=int)

# update G with true capacity edges only
G = nx.Graph(((u, v, e) for u, v, e in G.edges(data=True) if e['capacity'] == 1))

u = 1
v = 5

# determine all_simple_paths between requested nodes
paths = nx.all_simple_paths(G, u, v)

wps = []
#print("sorted simple paths %d to %d" % (u, v))
for path in nx.all_simple_paths(G, source=u, target=v):
    wp = path, nx.path_weight(G, path, weight='distance')
    if wp not in wps:
        wps.append(wp)

# setup a edge ref. array for the candidate & diverse route references
candidate_route_ref = []
diverse_route_ref = []

# loop through all available paths
for p in wps:
    #print(p, nx.path_weight(G, p, weight='distance') )
    
    # for p determine the ref. segments for all the edges
    edge_index = 0
    for l in len(p):
        attr = G[p[edge_index]][p[edge_index+1]]
        edge_index =+ 1
        edge_ref = attr["ref"]
        if candidate_route_ref == []:
            candidate_route_ref = candidate_route_ref.insert(edge_ref)
        else:
            candidate_route_ref = candidate_route_ref.remove(edge_ref)
            if diverse_route_ref == []:
                diverse_route_ref = diverse_route_ref.insert(edge_ref)
            else:
                diverse_route_ref = diverse_route_ref.remove(edge_ref)
        
        if candidate_route_ref != diverse_route_ref:
            print(candidate_route_ref)
            print(diverse_route_ref)