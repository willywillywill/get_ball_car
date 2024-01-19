import heapq


class config:
    car = 1
    boll = 2
    chick = 3
    no = 4

class node:
    def __init__(self, pos, car_node, struct):
        self.struct = struct
        self.pos = pos
        self.car_node = car_node
    def __lt__(self, other):
        return (((self.car_node.pos[0]-self.pos[0])**2 + (self.car_node.pos[1]-self.pos[1])**2)**0.5 <
                ((self.car_node.pos[0]-other.pos[0])**2 + (self.car_node.pos[1]-other.pos[1])**2)**0.5)
class graph:
    def __init__(self, car_pos):
        self.nodes = {}
        self.min_heap = []
        self.car_node = node(car_pos, config.car, config.car)

    def insert(self, pos, struct):
        self.nodes[pos] = node(pos=pos, struct=struct, car_node=self.car_node)
        heapq.heappush(self.min_heap, self.nodes[pos])
    def car_pos(self, new_pos):  #car
        self.car_node.pos = new_pos
    def to_pos(self):
        node = heapq.heappop(self.min_heap)
        self.car_pos(node.pos)
        return node
    def A_start(self, end):
        qu = [(0, *self.car_node.pos, [])]
        vis = []
        move = [(1, -1), (-1, 1), (-1, -1), (1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
        g = lambda n: abs(n[0] - self.car_node.pos[0]) + abs(n[1] - self.car_node.pos[1])
        h = lambda n: abs(end[0] - n[0]) + abs(end[1] - n[1])
        f = lambda n: g(n) + h(n)

        while qu:
            w,x,y,r = heapq.heappop(qu)

            vis.append((x,y))
            r.append((x,y))

            if (x,y) == end:
                return r
            for dx,dy in move:
                nx = x+dx
                ny = y+dy
                if (nx,ny) not in vis:
                    if (nx,ny) in self.nodes and self.nodes[(nx,ny)].struct == config.no:
                        continue
                    heapq.heappush(qu, (w+f((nx,ny)), nx, ny, r.copy()))
