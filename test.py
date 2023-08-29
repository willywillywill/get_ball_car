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
    
class Map_node(Node_state, Next):
    def __init__(self, node, size):
        self.size = size
        self.xy = (0,0)
        self.arr = [ [ node for i in range(self.size)] for j in range(self.size) ]
        
        self.next = Next()
    def updata(self, xy=None):
        if xy != None:
            self.next.add_data((xy[0],xy[1]))
        x,y = self.xy
        self.arr[x][y] = Node_state.state_dit[Node_state.no]
        
        x,y =  self.next.pop_data()
        self.arr[x][y] = Node_state.state_dit[Node_state.car]
    def return_data(self):
        return self.arr


ns = Node_state()
m = Map_node(ns.state_dit["no"],ns.Node_size)