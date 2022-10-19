import networkx as nx
import sys

try: 
    arg = sys.argv[1] 
except IndexError: 
    raise SystemExit(f"\nUsage: {sys.argv[0]} source_node target_node\n\ne.g.: python3 npt.py 1 5\n") 
    print(arg[::-1]) 

u = int(sys.argv[1])
v = int(sys.argv[2])

G = nx.Graph()
G = nx.read_edgelist("npt.edgelist", nodetype=int)

def capacity(path):
    return [(G[u][v]['capacity']) for (u,v)in zip(path[0:],path[1:])]
def spof(path):
    return [(G[u][v]['spof']) for (u,v)in zip(path[0:],path[1:])]
def ref(path):
    return [(G[u][v]['ref']) for (u,v)in zip(path[0:],path[1:])]

candidate_path = []
diverse_path = []

# determine all_simple_paths between requested nodes
paths = nx.all_simple_paths(G, u, v)

for p in paths:
    if not 0 in capacity(p):
        if candidate_path == []:
            candidate_path = p
            candidate_path_distance = nx.path_weight(G, p, weight='distance')
        else:
            diverse_path = p
            diverse_path_distance = nx.path_weight(G, p, weight='distance')
            if not any(item in ref(candidate_path) for item in spof(diverse_path)):
                print(candidate_path, candidate_path_distance)
                print(diverse_path, diverse_path_distance)
                candidate_path = []