import networkx as nx
import numpy as np
G = nx.Graph()
G.add_nodes_from(range(0,11))
G.add_edges_from([(0,3),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(3,4),(4,5),(4,6),(4,7),(4,8),(4,9),(4,10)])
adj=nx.adjacency_matrix(G)
centrality = nx.eigenvector_centrality(G)
clist=[centrality[node] for node in centrality]
print(centrality[7]*11/np.sum(clist))
print (np.sum(clist))