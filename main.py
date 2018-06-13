# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:43:51 2018
@author: Moc
"""

import networkx as nx
import nx_node_feature as nnf
#from nx_feature_get import *
from nx_graph_build import build_G

#节点序号标记转换
def Number_node(G):
    nodes = G.nodes()
    i = 0
    dict_num = {}
    for node in nodes:   
        i += 1
        dict_num[node] = i
    return dict_num
    
#建立新的网络，复制关系
def graph_new(G):
    G_new = nx.Graph()
    edges = G.edges()
    for edge in edges:
        G_new.add_edge(Number_node(G)[edge[0]], Number_node(G)[edge[1]])
    return G_new

#主函数      
if __name__ == '__main__':
    G = build_G()
#    list_node_old = GG.nodes()
    dict_num = Number_node(G)
#    print(dict_num)
    G_new = graph_new(G)
    list_node = G_new.nodes()
    dict_Du = nnf.Node_Du(G_new)
    dict_Week = nnf.week_range(G_new)
    dict_hide = nnf.Hi_DIP(G_new)
    dict_cycle = nnf.cyclic_coefficient_dip(G_new)
    dict_centrality = nnf.Centrality_DIP(G_new)
    dict_clustering = nnf.clustering_coefficient_DIP(G_new)
#    dict_rich_club = ng.rich_club_coefficient_dip(G_new) 不能实现
    list_all_feature = []
    for node in list_node:
        dict_all_feature = {}
        Du = dict_Du[node]
        Week = dict_Week[node]
        Hide = dict_hide[node]
        Cycle = dict_cycle[node]
        centrelity = dict_centrality[node]
        clustering = dict_clustering[node]
#        rich_club = dict_rich_club[node]
        list_node_feature = [Du, Week, Hide, Cycle, centrelity, clustering]
        #[节点度，节点脆弱性， 节点隐含信息， 节点环系数， 节点介数中心性, 节点聚类系数]
        for i in list(dict_num.keys()):
            if dict_num.get(i) == node:
                dict_all_feature[i] = list_node_feature
                list_all_feature.append(dict_all_feature)
    print(list_all_feature[:5])