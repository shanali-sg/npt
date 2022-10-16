# import networkx modules
import networkx as nx
G = nx.Graph()

# read edgelist from a file
G = nx.read_edgelist("npt.edgelist", nodetype=int)
G = nx.Graph(((u, v, e) for u,v,e in G.edges(data=True) if e['capacity'] == 1))

print("shortest paths")
for (u,v,e) in G.edges(data=True):
    print(nx.shortest_path(G, u, v, weight='distance'), e['distance'])

for (u,v,e) in G.edges(data=True):
    print("simple paths %d to %d" % (u, v))
    for path in nx.all_simple_paths(G, source=u, target=v):
        print(path, nx.path_weight(G, path, weight='distance'))

for (u,v,e) in G.edges(data=True):
    wps = []
    print("sorted simple paths %d to %d" % (u, v))
    for path in nx.all_simple_paths(G, source=u, target=v):
        wp = path, nx.path_weight(G, path, weight='distance')
        if wp not in wps:
                wps.append(wp)
    print(wps)

# update G with true capacity edges only
G = nx.Graph(((u, v, e) for u, v, e in G.edges(data=True) if e['capacity'] == 1))

# determine all_simple_paths between requested nodes
paths = nx.all_simple_paths(G, 1, 5)

# we need sorted paths
# sorted_paths = 

# setup a edge ref. array for the candidate & diverse route references
candidate_route_ref = []
diverse_route_ref = []

# loop through all available paths
for p in paths:
    #print(p, nx.path_weight(G, p, weight='distance') )
    
    # for p determine the ref. segments
    
         
    # if candidate_route_ref has no existing ref.
    # record the ref
    # if diverse_route_ref
    # record the ref
    # update candidate_route_ref & diverse_route_ref with subsequent 
    # reference to FALSE
    # if candidate_route_ref & diverse_route_ref are not equal has no FALSE
    # print the candidate_route & diverse_route from 
    # candidate_route_ref & diverse_route_ref
