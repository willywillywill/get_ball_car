from vpython import *
import time
import numpy as np
import matplotlib.pylab as plt
import pprint
import seaborn

Gsize = (50,50)
Cxy = (25,25)
Bxy = (0,0)
CNxy = (10,10)

Warr = np.zeros(shape=(Gsize[0],Gsize[1]), dtype=float)

class Chick_Node(standardAttributes):
    def __init__(self, pos = vector(0,5,0)):
        args = {}

        args['_default_size'] = vector(1, 1, 1)
        args['_objName'] = "box"
        args["pos"] = pos
        args["length"] = 1
        args["width"] = 1
        args["height"] = 0.5
        args["color"] = vector(1,1,0)

        super(Chick_Node, self).setup(args)

scene = canvas(title="test car", weight=500, height=500)

floor = box(pos=vector(0,0,0),length=50, height=0.5, width=50, color=vector(1,1,1))
floor2 = extrusion(
    path=paths.rectangle(width=50+2, height=50+2),
    shape=shapes.rectangle(width=2, height=0.5),
    color=vector(1,0,0)
    )

car  = box(pos=vector(Cxy[0],5,Cxy[1]),length=1, height=1, width=1, color=vector(0,0,1))
boll = box(pos=vector(Bxy[0],5,Bxy[1]),length=1, height=1, width=1, color=vector(0,1,0))
F_obj = {"car":car, "boll":boll}

n = 0


seaborn.heatmap(Warr)
plt.show()


"""
print(F_obj)

while 1:
    rate(1000)
    for i in F_obj:
        if F_obj[i].pos.y > (F_obj[i].height+floor.height)/2:
            F_obj[i].pos.y -= 0.01
        else:
            break
"""


