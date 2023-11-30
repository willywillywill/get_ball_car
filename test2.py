import time

import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
import pprint


class Node_state:
    ball = "ball"
    car = "car"
    no = "no"
    init = "init"
    state_dit = {init: 0.8, ball: 0.5, car: 1, no: 0}

    Node_size = 10


class Next:  # stack
    def __init__(self):
        self.data = []
    def add_data(self, data):
        self.data.append(data)
    def pop_data(self):
        return self.data.pop(-1)
    def return_data(self):
        return self.data


class Node(Node_state, Next):
    def __init__(self):
        self.xy = (Node_state.Node_size - 1, (Node_state.Node_size - 1)//2)  # car
        self.state_arr = [[Node_state.state_dit[Node_state.no if self.xy != (j, i) else Node_state.car]
                           for i in range(Node_state.Node_size)]
                          for j in range(Node_state.Node_size)]
        self.next = Next()

        next_node_xy = [0, Node_state.Node_size // 2]
        self.state_arr[next_node_xy[0]][next_node_xy[1]] = Node_state.state_dit[Node_state.init]
        self.next.add_data([next_node_xy[0], next_node_xy[1]])

    def add_ball(self, xy):
        self.state_arr[xy[0]][xy[1]] = Node_state.state_dit[Node_state.ball]
        self.next.add_data([xy[0], xy[1]])
    def updata_car(self, xy):
        xxyy = self.xy
        self.state_arr[xxyy[0]][xxyy[1]] = Node_state.state_dit[Node_state.no]

        self.state_arr[xy[0]][xy[1]] = Node_state.state_dit[Node_state.car]
        self.xy = (xy[0], xy[1])
    def pop_data(self):
        xy = self.next.pop_data()
        self.state_arr[xy[0]][xy[1]] = Node_state.state_dit[Node_state.no]
        return xy
    def return_state(self):
        return self.state_arr
    def return_xy(self):
        return self.xy


class Map(Next):
    def __init__(self, Msize):
        self.size = Msize
        self.xy = (0, 0)
        self.map = [[Node() for i in range(self.size)] for j in range(self.size)]
        self.next = Next()

    def updata_map(self, xy=None):
        if xy != None:
            self.next.add_data((xy[0], xy[1]))

        x, y = self.next.pop_data()
        self.xy = (x, y)
    def return_map(self):  # in map
        out = [[1 if self.xy == (i, j) else 0 for j in range(self.size)] for i in range(self.size)]
        return out




ns = Node_state()
Msize = 5
m = Map(Msize)

fig, ax = plt.subplots(1, 3)
im1 = ax[0].imshow(m.return_map())
im2 = ax[1].imshow(m.map[m.xy[0]][m.xy[1]].return_state())
im3 = ax[2].imshow(m.map[m.xy[0]][m.xy[1]].return_state())


def animate(i):
    ax[0].title.set_text("map-%d" % (i))
    ax[1].title.set_text("node-%d-car" % (i))
    ax[2].title.set_text("node-%d-ball" % (i))

    y = i // Msize
    x = abs(((Msize - 1) * (y % 2)) - (i % Msize))

    m.updata_map((x, y))
    im1_data = m.return_map()
    im1.set_data(im1_data)

    ball_random = np.random.randint(low=0, high=ns.Node_size, size=[np.random.randint(low=0, high=5, size=1)[0], 2])
    for j in ball_random:
        m.map[m.xy[0]][m.xy[1]].add_ball(j)
    im3_data = m.map[m.xy[0]][m.xy[1]].return_state()
    im3.set_data(im3_data)

    while len(m.map[m.xy[0]][m.xy[1]].next.return_data()) > 1:
        ball_xy = m.map[m.xy[0]][m.xy[1]].pop_data()
        car_xy = m.map[m.xy[0]][m.xy[1]].return_xy()
        dx = ball_xy[0]-car_xy[0]
        dy = ball_xy[1]-car_xy[1]

        for _ in range(abs(dx)):
            x,y = m.map[m.xy[0]][m.xy[1]].return_xy()
            m.map[m.xy[0]][m.xy[1]].updata_car( [x+1 if dx>0 else x-1 , y] )

        for _ in range(abs(dy)):
            x,y = m.map[m.xy[0]][m.xy[1]].return_xy()
            m.map[m.xy[0]][m.xy[1]].updata_car( [x , y+1 if dy>0 else y-1] )
        im2_data = m.map[m.xy[0]][m.xy[1]].return_state()
        im2.set_data(im2_data)


    return im1


d = [i for i in range(Msize * Msize)]
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=d + d[::-1],
                              interval=200)

plt.show()