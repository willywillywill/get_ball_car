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
    def updata(self): # !
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
        self.map = [ [ [Node, 0 if self.xy != (i,j) else 1] for i in range(self.size) ] for j in range(self.size) ]
        self.next = Next()
    def updata(self):
        x,y = self.xy
        self.map[x][y][1] = 0

        x,y = self.next.pop_data()
        self.map[x][y][1] = 1
        self.xy = (x,y)
    def return_map(self):
        x,y = self.xy
        return self.map[x][y].return_state()



ns = Node_state()
Msize = 5

map = Map(Msize)

fig, ax = plt.subplots(1,2)


