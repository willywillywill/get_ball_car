import time
from vpython import *
import random




class obj_info:
    def __init__(self, **kwargs):
        # 直接
        self.obj = kwargs["obj"]
        self.name = kwargs["name"]
        self.pos = vector(*kwargs["pos"])
        self.size = vector(*kwargs["size"])
        self.color = vector(*kwargs["color"])
        self.struct = kwargs["struct"]

        # 間接
        self.visible = True
        self.idx = (self.pos.x, self.pos.z)

    def set_pos(self, pos):
        if type(pos)==tuple:
            pos = vector(*pos)
        self.pos = pos
        self.idx = (pos.x,pos.z)
        self.obj.pos = pos

    def set_visible(self, tf):
        self.visible = tf
        self.obj.visible = tf

class space_Obj(object):
    grand_size = (10, 0.4, 10)
    grand_color = (1, 1, 1)
    boll_size = (0.4, 0.4, 0.4)
    boll_color = (3, 0, 0)
    car_size = (0.4, 0.4, 0.4)
    car_color = (0, 3, 0)
    obj_height = 0.4

    car_struct = 1
    grand_struct = -1
    no_struct = 0
    boll_struct = 2
    @classmethod
    def ground(cls, name):
        info = obj_info(
            name=name,
            size=cls.grand_size,
            obj=box, pos=(0,0,0),
            color=cls.grand_color,
            struct=cls.grand_struct
        )
        return info
    @classmethod
    def boll(cls, name, x=0,y=0):
        pos = (x, cls.obj_height, y)
        info = obj_info(
            name=name,
            pos=pos,
            size=cls.boll_size,
            obj=box,
            color=cls.boll_color,
            struct=cls.boll_struct
        )
        return info
    @classmethod
    def car(cls, name, x=0,y=0):
        pos = (x, cls.obj_height, y)
        info = obj_info(
            name=name,
            pos=pos,
            size=cls.car_size,
            obj=box,
            color=cls.car_color,
            struct=cls.car_struct
        )
        return info

class Space:
    def __init__(self):
        self.scene = canvas(background=color.white)
        self.scene.append_to_title("<dev>")
        self.scene.append_to_caption("<dev/>")
        self.obj_list = {}
    def add_obj(self, obj_):
        for i in self.obj_list:
            if self.obj_list[i].visible == False and type(self.obj_list[i].obj)==obj_.obj:
                self.obj_list[i].set_visible(True)
                self.obj_list[i].name = obj_.name
                self.obj_list[i].set_pos(obj_.pos)
                self.obj_list[i].size = obj_.size
                self.obj_list[i].color = obj_.color
                self.obj_list[i].struct = obj_.struct
                self.obj_list[obj_.name] = self.obj_list.pop(i)
                break
        else:
            name = obj_.name
            obj_.obj = obj_.obj(
                size =obj_.size,
                pos  =obj_.pos,
                color=obj_.color
            )
            self.obj_list[name] = obj_
    def updata_pos(self, name, x,y):
        pos = (x, 1,y)
        self.obj_list[name].set_pos(pos)
    def delete(self,name):
        self.obj_list[name].set_visible(False)

class route(space_Obj):
    def __init__(self, obj_lst):
        self.min_route = {"r": [], "w": 1e9}
        self.obj_lst = obj_lst

    def __dfs(self, w: float, root: tuple, ptr: tuple, vis: dict):
        if 0 not in vis.values():
            if self.min_route["w"] > w:
                self.min_route = {"r": vis, "w": w}
            return
        if vis[root] or self.min_route["w"] <= w:
            return
        vis[root] = vis[ptr] + 1
        for i in vis:
            if i != ptr:
                dw = ((i[0] - root[0]) ** 2 + (i[1] - root[1]) ** 2) ** 0.5
                self.__dfs(w + dw, i, root, vis.copy())
    def dfs(self, start):
        vis = {
            self.obj_lst[i].idx:0
            for i in self.obj_lst
            if self.obj_lst[i].struct==space_Obj.boll_struct
        }
        vis[start] = 0
        self.__dfs(0, start, start, vis)
        min_r = list(self.min_route["r"].items())
        min_r.sort(key=lambda x:x[1])
        return min_r



space = Space()
r = route(space.obj_list)
space.add_obj(space_Obj.ground("G"))
space.add_obj(space_Obj.car("C", 0,0))
for i in range(5):
    idx = (random.randint(-5,5),random.randint(-5,5))
    space.add_obj(space_Obj.boll(f"B{i}", *idx))

min_r = r.dfs(space.obj_list["C"].idx)
for i in min_r:
    idx = i[0]
    print(idx)
    space.updata_pos("C", idx[0], idx[1])
    time.sleep(1)