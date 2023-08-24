import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation

class Node:
    def __init__(self, xy):
        self.data = np.random.randint(2, size=(10,10))
        self.xy = xy
        self.next = None
    def insert_data(self, data):
        self.data.append(data)
    def pop_data(self):
        return  self.data.pop()
    def set_next(self, next):
        self.next = next
    def return_data(self):
        return self.data

class Map:
    def __init__(self,Msize):

        self.data = {

            "map":{
                "node": [ [Node((i,j)) for j in range(Msize)] for i in range(Msize)],
                "next": [],
                "xy"  : (0, 0),
                "size": Msize
            }

                     }
    # ALL node data
    def return_node_data(self, to:str):
        data = []
        for i in range(self.data[to]["size"]):
            data.append([])
            for j in range(self.data[to]["size"]):
                data[-1].append(self.data[to]["node"][i][j].return_data())

        return data
    def return_noe_data(self, to, x,y):
        return self.data[to]["node"][x][y].return_data()

    def updata(self, to:str):
        x,y = self.data[to]["next"].pop(0)
        self.data[to]["node"][ self.data[to]["xy"][0] ][ self.data[to]["xy"][1] ].set_next( self.data[to]["node"][x][y] )
        self.now_xy = (x,y)

    def A_mode(self, i:int, to:str):
        y = i // self.data[to]["size"]
        x = abs(((self.data[to]["size"] - 1) * (y % 2)) - (i % self.data[to]["size"]))

        self.data[to]["next"].append((x,y))
        self.updata(to)


Msize = 5

root = Map(5)
fig, ax = plt.subplots()

ll = root.return_noe_data("map",0,0)
im1 = ax.imshow(ll)
ax.title.set_text("MAP")

def animate(i):
    y = i // Msize
    x = i % Msize

    root.A_mode(i, "map")
    im1.set_data(root.return_noe_data("map",x,y))
    return im1

d = [ i for i in range(Msize*Msize) ]
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=d+d[::-1],
                              interval=200)


