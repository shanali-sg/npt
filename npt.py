import networkx as nx
import sys

try: 
    arg = sys.argv[1] 
except IndexError: 
    raise SystemExit(f"\nUsage: {sys.argv[0]} source_node target_node\n\ne.g.: python3 npt.py 1 5\n") 
    print(arg[::-1]) 

u = int(sys.argv[1])
v = int(sys.argv[2])

# initaliztion various list variables
candidateDiversePath = []
diversePathList = []
shortestPathRef = []
shortestPath = []
commonRefs = []

shortestPathDistance = 0

G = nx.Graph() # Initialize Graph G for our network
H = nx.Graph() # Graph H in case if valid diverse paths are not found in G
G = nx.read_edgelist("npt.edgelist", nodetype=int)
G = nx.Graph(((u, v, e) for u, v, e in G.edges(data=True) if e['capacity'] == 1)) # Update G with capacity available edges only

def edge_attr(graph, path, edge_attr):
    return [(graph[u][v][edge_attr]) for (u,v)in zip(path[0:],path[1:])]

def isListEmpty(inList):
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList) )
    return False

def pathDistance(path):
    return nx.path_weight(G, path, weight = 'distance')

# determine all simple_paths between requested nodes
paths = nx.all_simple_paths(G, u, v)

# determine shortest Path & Distance between requested nodes
spath = nx.shortest_path(G, u, v, weight = 'distance')
spathDistance = pathDistance(spath)
spathRef = edge_attr(G, spath, 'ref')

candidateShortestPath = spath
candidateShortestPathDistance = spathDistance
candidateShortestPathRef = edge_attr(G, candidateShortestPath, 'ref')

# iterate through all paths for a diverse pair
for p in paths:
    candidateDiversePath = p
    candidateDiversePathSpof = edge_attr(G, candidateDiversePath, 'spof')

    commonRefs = [list(filter(lambda x: x in list(candidateShortestPathRef), sublist)) for sublist in list(candidateDiversePathSpof)]

    if not(candidateShortestPath == candidateDiversePath) and isListEmpty(commonRefs):
        shortestPath = candidateShortestPath
        shortestPathDistance = candidateShortestPathDistance
        shortestPathRef = candidateShortestPathRef
        diversePathList.append(candidateDiversePath)

    if diversePathList == []:
        # if no protected path pairs were found then explore diverse path pair using 2nd shortest path pair as worker
        H = nx.Graph((u, v, e) for u, v, e in G.edges(data=True) if (e['capacity'] == 1) and (e['ref'] is not candidateShortestPathRef[0]))
        candidateShortestPath = nx.shortest_path(H, u, v, weight = 'distance')
        candidateShortestPathDistance = nx.path_weight(G, candidateShortestPath, weight = 'distance')
        candidateShortestPathRef = edge_attr(H, candidateShortestPath, 'ref')

diversePathList.sort(key=pathDistance)

print("Shortest Path:")
print("Shortest Path is                      : ", f"{spathDistance:9.3f}", spath)
print("Shortest Path Ref List is             :           ", spathRef)
print("\n")
print("Diverse Paths:")
print("Worker Path distance is               : ", f"{shortestPathDistance:9.3f}", shortestPath)
print("Worker Path Ref List is               :           ", shortestPathRef)
print("Protected path distance is            : ", f"{nx.path_weight(G, diversePathList[0], weight = 'distance'):9.3f}", diversePathList[0])
print("Protected path Ref list is            :           ", edge_attr(G, diversePathList[0], 'ref'))