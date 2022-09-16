
if __name__ == '__main__':
    class TestA(object):
        attr = 1


    obj_a = TestA()
    obj_b = TestA()
    obj_a.attr=24
    print(obj_a.attr)
    print(obj_b.attr)
    print(obj_a.__dict__)
    print(obj_b.__dict__)