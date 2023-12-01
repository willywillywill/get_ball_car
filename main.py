# from vpython import *
import numpy as np
import heapq

class node:
    def __init__(self, idx):
        self.idx = idx
class Link_list:
    def __init__(self):
        self.link = {}
        self.all_node = []
        self.all_idx = []
    def insert(self, idx):
        self.all_idx.append(idx)
        self.all_node.append(node(idx))
        for i in self.link:
            self.link[i].append(self.all_node[-1])
        self.link[self.all_node[-1]] = [ i for i in self.link ]

class Graph:
    def __init__(self):
        self.link = Link_list()
        self.xy = (0,0)
    def updata(self, idx:tuple):
        self.link.insert(idx)
    def dijkstra(self):
        qu = [(0, self.xy)]
        vis = { i.idx:0 for i in self.link.link }
        route = []
        heapq.heapify(qu)
        while qu:
            w,idx = heapq.heappop(qu)
            if vis[idx]:
                continue
            vis[idx] = 1
            route.append(idx)

            for i in self.link.link:
                d_w = ((i.idx[0]-idx[0])**2+(i.idx[1]-idx[1])**2)**0.5
                heapq.heappush(qu, (w+d_w,i.idx))
        print(route)
    def find_ptr(self, x):
        pass
    def kruskal(self):
        pass

graph = Graph()
graph.updata((0,0))
graph.updata((0,1))
graph.updata((1,0))
graph.updata((1,1))
graph.updata((2,1))
graph.updata((1,2))

graph.dijkstra()
