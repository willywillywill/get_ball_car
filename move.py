
class node:
    def __init__(self):
        """
        0: no
        1: car
        2: ball
        """
        self.struct = 0
class node_list:
    def __init__(self):
        self.all_node = {}

    def insert(self, idx:tuple, struct=0):
        self.all_node[idx] = node()
        self.all_node[idx].struct = struct
    def updata_struct(self, idx, val):
        self.all_node[idx].struct = val
    def updata_idx(self, old_idx, new_idx):
        self.all_node[new_idx] = self.all_node.pop(old_idx)


class route:
    def __init__(self, node_lst):
        self.min_route = {"r": [], "w": 1e9}
        self.node_lst = node_lst
    def dfs(self, w:float, root:tuple, ptr:tuple, vis:dict):
        if 0 not in vis.values():
            if self.min_route["w"] > w:
                self.min_route = {"r": vis, "w": w}
            return
        if vis[root] or self.min_route["w"] <= w:
            return
        vis[root] = vis[ptr] + 1
        for i in vis:
            if i != ptr:
                dw = ((i[0]-root[0])**2+(i[1]-root[1])**2)**0.5
                self.dfs(w+dw, i, root, vis.copy())

    def run(self, start:tuple):
        vis = { i:0 for i in self.node_lst.all_node if self.node_lst.all_node[i].struct==2 }
        self.dfs(0, start, start, vis)
        r = self.min_route["r"]
        w = self.min_route["w"]
        print(r, w)


""" test
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
"""
