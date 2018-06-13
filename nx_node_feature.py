# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:31:57 2018
@author: Moc
"""

import networkx as nx
import math


#1. 节点的度
def Node_Du(G):
    dict_Du = {}
    b = G.degree()
    for i in b:
        dict_Du[i[0]] = i[1]
    return dict_Du
    
    
#2. 节点脆弱性
def week_range(G):
    dict_1 = nx.all_pairs_shortest_path_length(G)   #计算所有的节点之间的最短距离，并存储在字典中 
    R = 0 
    for k1 in dict_1:
        for k in list(k1[1].values()):
            if k != 0:
                R=R+(1.0/(k))
#                print(R)
    N=nx.number_of_nodes(G) #计算网络节点数 
    E=(1.0/(N*(N-1)))*R #计算网络的整体效率 
    nodes=G.nodes() #返回图的节点列表 
    dict_week = {}
    for c in nodes:
        
        GG=G.copy()
        GG.remove_node(c)#删除节点 c 和它所连接的边 
        n=nx.number_of_nodes(GG)
        dict_2=nx.all_pairs_shortest_path_length(GG) #计算所有的节点之间的最短距离，并存储在字典中 
        r=0
        for k2 in dict_2:
            for k3 in list(k2[1].values()):
                if k3 != 0:
                    r = r + (1.0/(k3))
        e = (1.0/(n*(n - 1)))*r #计算删除节点 c 后网络的整体效率
        cuiruo = (E-e)/E  #脆弱性公式
#        print('节点 ', c,' 的脆弱性为： ', cuiruo)
        dict_week[c] = cuiruo
    return dict_week
    
    
#3. 节点隐含信息
def Sib_(sou,tar,G):#定义函数计算搜索信息 
    if nx.has_path(G,sou,tar):#判断是否存在路径 
        path=([p for p in nx.all_shortest_paths(G,source=sou,target=tar)])#返回路径列表 
        for l in path:#遍历路径 
            EPib=0 
            s=1.0  
            for j in l:#遍历路径中所有节点 
                if j in l and G.degree(j)>1:#排除源节点和目标节点,判断节点是否存在于路径中,j点度应该大于 1  
                    s*=(1.0/(G.degree(j)-1))  
            Pib=(1.0/G.degree(sou))*s  
            EPib+=Pib 
            sib=-math.log(EPib,2) 
            return sib 
    return 0
    
def Hi_DIP(G): #定义函数计算隐含信息  
    N=nx.number_of_nodes(G) 
    Node=G.nodes()  
    h=0 
    dict_hide = {}
    for k in Node:# 
        
        sum=0 
        h=h+1    
        for i in Node:     
            if k!=i: 
                Sib=Sib_(k,i,G) 
                sum+=Sib 
        Ai=(1.0/N)*sum# 
        dict_hide[k] = Ai  #key为节点k， value为隐含信息Ai的字典
    return dict_hide

    
#4. 节点环系数
def cyclic_dip(n,G):#定义公式计算节点的环系数（cyclic_coefficient）
    l=[]
    c=nx.cycle_basis(G)#求出图中的所有环
    for i in c :#求出含节点 n 的环并保存在列表 l 中 
        if n in i:
            l.append(i)
    def f(x):#求长度的函数
        return len(x)
    if len(l)==0:
        return 'no cyclic'
    else:
        l.sort(key=f)#根据列表元素的长度排序
        minl=len(min(l,key=f))#计算最小环的长度
        L=[]
        for j in l:#求出最短环的集合并保存在列表 L 中
            if len(j)==minl:
                L.append(j)
    du=G.degree(n)#求出所有节点的度
    sum=0.0
    for k in L:
        sum+=1.0/minl
    Oi=(1.0/(du*(du-1)))*sum
    return Oi

def cyclic_coefficient_dip(G):#定义函数计算网络的环系数
    node=G.nodes()#计算网络的节点
    dict_cycle = {}
    for n in node:
        Oi=cyclic_dip(n,G) #计算网络中所有节点的环系数
        if Oi != 'no cyclic':
            dict_cycle[n] = Oi   
        else:
            dict_cycle[n] = ""
    return dict_cycle

    
#5. 节点的 betweenness centrality 介数中心性
def Centrality_DIP(G):
    B=nx.betweenness_centrality(G)#计算每个节点的（betweenness centrality），存储在字典中 
    dict_centrality = {}
    for i in B:
        dict_centrality[i] = B[i]
    return dict_centrality

    
#6. 节点聚类系数
def clustering_coefficient_DIP(G): #定义公式计算每个节点的 clustering_coefficient G=create_network()#调用公式，构建网络  
    C=nx.clustering(G)#获取节点的聚类系数
    dict_clustering = {}
    for n in C:#逐一提出节点的聚类系数
        dict_clustering[n] = C[n] #节点聚类系数 
    return dict_clustering        
    
#7. 节点富人俱乐部系数
#def rich_club_coefficient_dip(G):#定义函数计算网络的 rich club coefficient 
#    RC=nx.rich_club_coefficient(G)#计算网的 rich club coefficient
#    print(RC)
#    dict_rich_club = {}
#    for k in RC:
#        print(k)
#        dict_rich_club[k]=RC[k] #rich_club_coefficient
#    return dict_rich_club

    
    
    
    
    
    
    
    









    
