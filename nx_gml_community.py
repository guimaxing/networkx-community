# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:55:56 2018

@author: Administrator
"""

import networkx as nx 
import matplotlib.pyplot as plt 
from nx_graph_build import build_G
import community
#G = nx.read_gml(r"C:\Users\Administrator\Desktop\dolphins.gml")
G = build_G()

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))

#cliques 小圈子， nx.number_of_cliques(G, nodes = 'TR77') 返node所处的圈子位置。
#nx.number_of_cliques(G) 返回所有节点和所在的圈子，以{node：num} 字典的形式。
print(nx.number_of_cliques(G, nodes = 'TR77'))
#list of k-cliques in the network. each element contains the nodes that consist the clique.
klist = list(nx.community.k_clique_communities(G,3))
print(len(klist))
#小圈子中nx.community.k_clique_communities(G,k) k个点要求是相互有联系，既之前都有线相连， 多个小圈子组成的社区

#通过设置不同的k值，圈出的社区数量也会随之变化
#for k in range(3,6):
#    klist_new = list(nx.community.k_clique_communities(G,k))
#    print(len(klist_new))

#去除在社区中的节点，留下不属于任何社区的节点
aa = list(G.nodes())
list_1 = []
for item in klist:
    list_1.extend(item)
bb = list(set(list_1))
for node in bb:
    if node not in aa:
        pass
    else:
        aa.remove(node)
#aa不属于任何社区的节点列表
pos = nx.spring_layout(G)
plt.clf()
fig = plt.figure(figsize=(10, 8), facecolor='white')
#nx.draw(G,pos = pos, with_labels=True)
nx.draw(G,pos = pos, nodelist = aa, node_color = 'r', with_labels=True)
nx.draw(G,pos = pos, nodelist = klist[0], node_color = 'b')
nx.draw(G,pos = pos, nodelist = klist[1], node_color = 'y')
nx.draw(G,pos = pos, nodelist = klist[2], node_color = 'g')
nx.draw(G,pos = pos, nodelist = klist[3], node_color = 'black')
plt.show()

#查找在社群中的点
#if 'TR77' in bb:
#    for i in range(0, len(klist), 1):
#        if 'TR77' in klist[i]:
#            print(i)
#            print(klist[i])
#            nx.draw(G,pos = pos, nodelist = klist[i], node_color = 'y')
#            plt.show()
##        if 'Jonah' in klist[i]:
##            print(i)
##            print(klist[i])
##            nx.draw(G,pos = pos, nodelist = klist[i], node_color = 'g')
##            plt.show()
#
#if 'TR82' in aa:
#    print('该节点不属于任何一个社区合集')
#    print(aa)
#    nx.draw(G,pos = pos, nodelist = aa, node_color = 'r')
#    plt.show()


partition = community.community_louvain.best_partition(G)
#list_11 = []
#for com in set(partition.values()):
#    list_nodes = [nodes for nodes in partition.keys()
#                            if partition[nodes] == com]    
#    list_11.append(list_nodes)
#print(len(list_11))

size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
list_all = []
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]                 
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 50,
                                node_color = str(count / size))
    list_all.append(list_nodes)
nx.draw_networkx_edges(G,pos,with_labels = True, alpha=0.5 )
plt.show()    

fig = plt.figure(figsize=(12, 9), facecolor='white')
nx.draw(G, pos, node_size = 300, with_labels=True)
nx.draw(G,pos = pos, nodelist = list_all[0], node_size = 300, node_color = 'b', with_labels=True)
nx.draw(G,pos = pos, nodelist = list_all[1], node_size = 300, node_color = 'g', with_labels=True)
nx.draw(G,pos = pos, nodelist = list_all[2], node_size = 300, node_color = 'y', with_labels=True)
nx.draw(G,pos = pos, nodelist = list_all[3], node_size = 300, node_color = 'black', with_labels=True)
nx.draw(G,pos = pos, nodelist = list_all[3], node_size = 300, node_color = '0.5', with_labels=True)