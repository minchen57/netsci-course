import os
import pandas
import numpy as np
import networkx as nx
relativepath = os.getcwd()
datapath = relativepath + "/data/migraine_authors.csv"
data = pandas.read_csv(datapath)
data.columns =["author1", "author2","count"]
print (data.columns)
print (len(data))
print (data.head(5))

G = nx.Graph()
for idx, row in data.iterrows():
    if not G.has_node(row.author1):
        G.add_node(row.author1)
    if not G.has_node(row.author2):
        G.add_node(row.author2)
    G.add_edge(row.author1,row.author2)
print(nx.info(G))
nx.write_gml(G,relativepath + "/data/migraine_authors.gml")