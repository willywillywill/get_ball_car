import threading
import json

def read_json_data():
    with open("test.json", "r") as f:
        try:
            d = json.load(f)
        except:
            d = {}
    return d

class node_obj:
    def __init__(self, **kwargs):
        assert kwargs["name"],kwargs["fun"]
        self.file = "test.json"
        self.name = kwargs["name"]
        self.fun = kwargs["fun"]
        self.read = kwargs["read"] if "read" in kwargs else None
        del kwargs["fun"]
        del kwargs["name"]

        kwargs["return_val"] = None
        d = read_json_data()
        with open(self.file, "w") as f:
            d[self.name] = kwargs
            json.dump(d, f)
    def set_reader(self, read_name:str):
        self.read = read_name
    def run(self):
        d = read_json_data()
        if self.read: d[self.name] = {"return_val":self.fun(d[self.read]["return_val"])}
        else:   d[self.name] = {"return_val":self.fun()}
        with open(self.file, "w") as f:
            json.dump(d, f)
    def return_file(self):
        return read_json_data()

def test():
    return 10
def test2(val):
    return val+10

n1 = node_obj(name="test1", fun=test)
n2 = node_obj(name="test2", fun=test2).set_reader("test1")
n3 = node_obj(name="test3", fun=test2).set_reader("test1")

