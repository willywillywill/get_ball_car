import numpy as np
import pprint


class Node_state:
    ball = "ball"
    car = "car"
    no = "no"
    init = "init"
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
        self.state_arr = [[ Node_state.no if self.xy != (j, i) else Node_state.car
                           for i in range(Node_state.Node_size)]
                          for j in range(Node_state.Node_size)]
        self.next = Next()

        next_node_xy = [0, Node_state.Node_size // 2]
        self.state_arr[next_node_xy[0]][next_node_xy[1]] = Node_state.init
        self.next.add_data([next_node_xy[0], next_node_xy[1]])

    def add_ball(self, xy):
        self.state_arr[xy[0]][xy[1]] = Node_state.ball+str(len(self.next.return_data()))
        self.next.add_data([xy[0], xy[1]])
    def updata_car(self, xy):
        xxyy = self.xy
        self.state_arr[xxyy[0]][xxyy[1]] = Node_state.no

        self.state_arr[xy[0]][xy[1]] = Node_state.car
        self.xy = (xy[0], xy[1])
    def pop_data(self):
        xy = self.next.pop_data()
        self.state_arr[xy[0]][xy[1]] = Node_state.no
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

def M_move_xy(i):
    y = i // Msize
    x = abs(((Msize - 1) * (y % 2)) - (i % Msize))
    return [x,y]

ns = Node_state()
Msize = 5
m = Map(Msize)
ball_num = 0
e = 0

out = m.map[0][0].return_state()
print("init")
pprint.pprint(out)

ball_random = np.random.randint(low=0, high=ns.Node_size, size=[np.random.randint(low=0, high=5, size=1)[0], 2])
for i in ball_random:
    m.map[0][0].add_ball(i)
    out = m.map[0][0].return_state()
    print("add : ",i)
    pprint.pprint(out)

while m.map[0][0].next.return_data():
    xy = m.map[0][0].pop_data()
    ball_num+=1
    m.map[0][0].updata_car(xy)
    if ball_num >=3:
        m.map[0][0].add_ball([ns.Node_size - 1, (ns.Node_size - 1)//2])
        xy = m.map[0][0].pop_data()
        m.map[0][0].updata_car(xy)
        ball_num=0
        out = m.map[0][0].return_state()
        print("cls : ", xy)
        pprint.pprint(out)
    else:
        out = m.map[0][0].return_state()
        print("pop : ", xy)
        pprint.pprint(out)
