import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
import pprint

class Node:
    def __init__(self, xy):
        self.data = np.random.randint(2, size=(10,10))
        self.xy = xy
        self.next = None
        self.node_state_dit = {"car":1, "no":0}
        self.node_state = self.node_state_dit["no"]
    def set_state(self, state):
        self.node_state = self.node_state_dit[state]
    def set_data(self, x,y, data):
        self.data[x][y] = data
    def set_next(self, next):
        self.next = next
    def return_state(self):
        return self.node_state
    def return_data(self):
        return self.data
    def return_xy(self):
        return self.xy

class Map:
    def __init__(self,Msize):
        self.node = [ [Node((i,j)) for j in range(Msize)] for i in range(Msize)]
        self.next = []
        self.xy = (0,0)
        self.size = Msize
    def return_data(self, x,y):
        return self.node[x][y].return_data()
    def return_datas(self):
        data = [
            [self.return_data(i, j) for j in range(self.size)]
            for i in range(self.size)
        ]
        return data
    def return_node_state(self,x,y):
        return  self.node[x][y].return_state()
    def return_nodes_state(self):
        data = [
                [ self.return_node_state(i,j) for j in range(self.size) ]
                for i in range(self.size)
                ]
        return np.array(data)
    def add_next(self, x,y):
        self.next.append((x,y))
    def updata(self):
        x,y = self.next.pop(0)
        self.node[self.xy[0]][self.xy[1]].set_next(self.node[x][y])
        self.node[self.xy[0]][self.xy[1]].set_state("no")
        self.node[x][y].set_state("car")
        self.xy = (x,y)
    def A(self, i):
        y = i // self.size
        x = abs(((self.size - 1) * (y % 2)) - (i % self.size))
        self.add_next(x,y)
        self.updata()
        return x,y


Msize = 5
root = Map(Msize)
fig, ax = plt.subplots(1,2)

ax[0].title.set_text("MAP")
im1 = ax[0].imshow(root.return_data(0,0))
im2 = ax[1].imshow(root.return_nodes_state())

def animate(i):

    x,y = root.A(i)

    j = root.return_nodes_state()
    k = root.return_data(x,y)
    pprint.pprint(j)
    im1.set_data(k)
    im2.set_data(j)

    return im1

d = [ i for i in range(Msize*Msize) ]
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=d+d[::-1],
                              interval=200)


