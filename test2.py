import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation

class Node:
    def __init__(self, cnt=0):
        self.data = []
        self.next = None
        self.cnt = cnt
    def insert_next(self):
        if self.next:
            self.next.insert_next()
        else:
            self.next = Node(cnt=self.cnt+1)
    def insert_data(self, cnt, data):
        if self.cnt == cnt:
            self.data.append(data)
        else:
            self.next.insert_data(cnt=cnt, data=data)
    def pop_data(self, cnt):
        if self.cnt == cnt:
            self.data.pop(-1)
        else:
            self.next.pop_data(cnt=cnt)
    def ALL_Node(self, lst=[]):
        lst.append(self.data)
        if self.next:
            self.next.ALL_Node()
        return lst
    def ONE_Node(self, cnt):
        return self.ALL_Node()[cnt]

Msize = 5
Wsize = 5
Map = np.zeros((Msize, Msize))
Warr = np.random.randint(2, size=(Wsize,Wsize))
Map[0][0]=1

tree = Node()

for i in range(Msize * Msize):
    y = i // Msize
    x = abs(((Msize - 1) * (y % 2)) - (i % Msize))

    tree.insert_next()
    tree.insert_data(cnt=i, data=(x,y))

fig, ax = plt.subplots(1,2)
im1 = ax[0].imshow(Map)
im2 = ax[1].imshow(Warr)
ax[0].title.set_text("MAP")
ax[1].title.set_text("Warr")

lst = tree.ALL_Node()
del lst[-1]

def animate(i):
    Warr = np.random.randint(2, size=(Wsize,Wsize))
    xy = np.where( Warr == 1 )
    Warr[xy[0]][xy[1]] = 1
    im2.set_data(Warr)
    for j in xy:
        tree.insert_data(i, j)

    while len(tree.ONE_Node(i)) != 1:
        tree.pop_data(i)
        print(tree.ONE_Node(i))

    Warr[xy[0]][xy[1]] = 0
    im2.set_data(Warr)

    x,y = lst[i][0]
    Map[x][y]=1
    im1.set_data(Map)
    Map[x][y] = 0

    return im1

d = [ i for i in range(len(lst)) ]
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=d+d[::-1],
                              interval=200)


