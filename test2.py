import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
import pprint

class Node_state:
    ball = "ball"
    car = "car"
    no = "no"
    state_dit = { ball:2, car:1, no:0 }

    Node_size = 10

class Next:  # stack
    def __init__(self):
        self.data = []
    def add_data(self, data):
        self.data.append(data)
    def pop_data(self):
        return self.data.pop(-1)

class Node(Node_state, Next):
    def __init__(self):
        self.xy = (0, 0)
        self.state_arr = [ [ Node_state.state_dit[Node_state.no if self.xy != (i,j) else Node_state.car]
                             for i in range(Node_state.Node_size) ]
                           for j in range(Node_state.Node_size) ]
        self.next = Next()
    def updata(self, xy=None): # !
        if xy!=None:
            self.next.add_data((xy[0],xy[1]))
        x,y = self.xy
        self.state_arr[x][y] = Node_state.state_dit[Node_state.no]

        x,y = self.next.pop_data()
        self.state_arr[x][y] = Node_state.state_dit[Node_state.car]
        self.xy = (x,y)
    def return_state(self):
        return self.state_arr
    
class Map(Next):
    def __init__(self, Msize):
        self.size = Msize
        self.xy = (0,0)
        self.map = [ [ Node() for i in range(self.size) ] for j in range(self.size) ]
        self.next = Next()
    def updata_map(self, xy=None):
        if xy!=None:
            self.next.add_data((xy[0],xy[1]))

        x,y = self.next.pop_data()
        self.xy = (x,y)
    def update_node(self, xy=None):
        x,y = self.xy
        self.map[x][y].updata(xy)
    def return_node(self):  # in node 
        x,y = self.xy
        return self.map[x][y].return_state()
    def return_map(self): # in map
        out = [ [ 1 if self.xy==(i,j) else 0 for j in range(self.size) ] for i in range(self.size) ]
        return out


ns = Node_state()
Msize = 5
m = Map(Msize)

fig, ax = plt.subplots(1,2)
im1 = ax[0].imshow(m.return_map())
im2 = ax[1].imshow(m.return_node())

def animate(i):
    ax[0].title.set_text("map-%d" % (i))
    ax[1].title.set_text("node-%d" % (i))

    y = i // Msize
    x = abs(((Msize - 1) * (y % 2)) - (i % Msize))

    m.updata_map((x,y))
    

    im1_data = m.return_map()
    im2_data = m.return_node()
    
    im1.set_data(im1_data)
    im2.set_data(im2_data)

    return im1

d = [ i for i in range(Msize*Msize) ]
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=d+d[::-1],
                              interval=200)

plt.show()