from test import node_obj

def test():
    return 10
t1 = node_obj(name="test", fun=test)

print(t1.return_file())