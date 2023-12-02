# from vpython import *
import numpy as np
import heapq

class node:
    def __init__(self, idx):
        self.idx = idx
        """
        0: no
        1: car
        2: ball
        """
        self.struct = 0
class node_list:
    def __init__(self):
        self.all_node = []
        self.all_idx = []
    def insert(self, idx:tuple):
        root = node(idx)
        self.all_idx.append(idx)
        self.all_node.append(root)
    def updata_struct(self, idx, val):
        idx = self.all_idx.index(idx)
        self.all_node[idx].struct = val

class route:
    def __init__(self, node_lst):
        self.min_route = {"r": [], "w": 1e9}
        self.node_lst = node_lst
    def dfs(self, w:float, root:node, ptr:node, vis:dict):
        if 0 not in vis.values():
            if self.min_route["w"] > w:
                self.min_route = { "r":vis, "w":w }
            return
        elif vis[root]:
            return

        vis[root] = vis[ptr]+1
        for i in vis:
            if i != ptr:
                dw = ((root.idx[0]-i.idx[0])**2 + (root.idx[1]-i.idx[1])**2)**0.5
                self.dfs(w+dw, i, root, vis.copy())

    def run(self, start:tuple):
        vis = { i:0 for i in self.node_lst.all_node if i.struct==2 }
        root = self.node_lst.all_node[self.node_lst.all_idx.index(start)]
        self.dfs(0, root, root, vis)
        r = self.min_route["r"]
        w = self.min_route["w"]
        print([ [i.idx, r[i]] for i in r ], w)



graph = node_list()
graph.insert((0,0))
graph.insert((1,9))
graph.insert((5,2))
graph.insert((3,5))

graph.updata_struct((0,0), 2)
graph.updata_struct((5,2), 2)
graph.updata_struct((3,5), 2)


r = route(graph)
r.run((0,0))
