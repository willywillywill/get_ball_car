import time
from vpython import *

class obj_info:
    def __init__(self, **kwargs):
        if "pos" not in kwargs:
            kwargs["pos"] = (0,0,0)
        if "color" not in kwargs:
            kwargs["color"] = (1,1,1)

        self.name = kwargs["name"]
        self.pos = vector(*kwargs["pos"])
        self.obj = kwargs["obj"]
        self.size = vector(*kwargs["size"])
        self.color = vector(*kwargs["color"])
class Obj:
    def __init__(self):
        self.grand_size = (10, 0.4, 10)
        self.boll_size = (1, 1, 1)
        self.boll_color = (255,0,0)
    def grand(self, name):
        info = obj_info(name=name, size=self.grand_size, obj=box)
        return info
    def boll(self, name, pos:tuple=(0,0,0)):
        info = obj_info(name=name, pos=pos, size=self.boll_size, obj=box, color=self.boll_color)
        return info
    def car(self, name, pos:tuple=(0,0,0)):
        info = obj_info
        return info

class Scan:
    def __init__(self):
        self.obj_list = []
        self.name_list = []
    def add_obj(self, obj_):
        for i in self.obj_list:
            if i.visible == False and type(i)==obj_.obj:
                i.visible = True
                idx = self.obj_list.index(i)
                self.name_list[idx] = obj_.name
                self.obj_list[idx].pos = obj_.pos
                self.obj_list[idx].size = obj_.size
                self.obj_list[idx].color = obj_.color
                break
        else:
            name = obj_.name
            root = obj_.obj(
                size=obj_.size,
                pos =obj_.pos,
                color=obj_.color
            )
            self.obj_list.append(root)
            self.name_list.append(name)
        print(self.name_list)
    def updata_pos(self, name, pos):
        idx = self.name_list.index(name)
        self.obj_list[idx].pos = vector(*pos)
    def delete(self,name):
        idx = self.name_list.index(name)
        self.obj_list[idx].visible = False



obj = Obj()
scan = Scan()
scan.add_obj(obj.grand("G"))
