from move import *
from scan import *

import random


graph = node_list()
r = route(graph)
space = Space()
space.add_obj(space_Obj.ground("G"))
space.add_obj(space_Obj.car("C"))
graph.insert((0,0), 1)

for i in range(5):
    idx = (random.randint(-5,5),random.randint(-5,5))
    graph.insert(idx)
    graph.updata_struct(idx, 2)
    space.add_obj(space_Obj.boll(f"B{i}"))
    space.updata_pos(f"B{i}", *idx)
