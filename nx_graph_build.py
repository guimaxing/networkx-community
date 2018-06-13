# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:35:16 2018
@author: Moc
"""
#社交网络数据
#from hg_nx_projects.nx_create_neworkx import create_network
#G = create_network()

import networkx as nx 
#import numpy as np 

def build_G():
#社团关系网络数据
    G = nx.read_gml("./dolphins.gml")
    print('完成网络建立')
    return G
