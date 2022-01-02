# This file is mainly used to extract information using NetworkX package, mainly to extract info that Gephi does not provide immediately.

import pandas as pd
import networkx as nx


G=nx.Graph()
df_nodes=pd.read_csv('nodes.csv')
df_edges=pd.read_csv('edges.csv')


print(nx.info(G))


for index, row in df_nodes.iterrows():
    G.add_node(row['Label'])
    
for index, row in df_edges.iterrows():
    G.add_weighted_edges_from([(row['Source'], row['Target'], row['Label'])])



density = nx.density(G)
print("Network density: %.4f" % density)


bridges=list(nx.bridges(G))
local_bridges=list(nx.local_bridges(G))

for bridge in bridges:
    print(bridge)

for local in local_bridges:
    print(local)

cliques = list(nx.find_cliques(G))

clique_number = len(list(cliques))
print(clique_number)




print("%.4f"% nx.degree_assortativity_coefficient(G))




