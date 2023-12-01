# from vpython import *
import numpy as np
import heapq
class Link_list:
    def __init__(self):
        self.link = {}
    def insert(self, val_idx):
        self.link[val_idx] = [ i for i in self.link ]
        for i in self.link:
            if i != val_idx:
                self.link[i].append(val_idx)
    def delete(self, idx):
        del self.link[idx]
        for i in self.link:
            if idx in self.link[i]:
                j = self.link[i].index(idx)
                del self.link[i][j]

class Graph:
    def __init__(self, shape):
        self.weight = np.zeros(shape, dtype=np.float16)
        self.link = Link_list()
    def updata(self, idx:tuple, w:int):
        self.weight[idx[0],idx[1]] = w
        self.link.insert(idx)
    
    def dijkstra(self, start, end):
        qu = [start]
        vis = { i:0 for i in self.link }
        heapq.heapify(qu)
        while qu:
            root = heapq.heappop(qu)
            if end == root:
                break
            if vis[root]:
                continue
            vis[root] = 1

            for i in self.link[root]:
                qu.append(i)
    def print_w(self):
        print(self.weight)
graph = Graph((10,10))
graph.updata((1,1),2)

graph.print_w()