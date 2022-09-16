u=10
def curve_pre():
    d=7
    c=5
    b=3
    a = 10
    def curve(x):
        print(u)
        return  a+b+c+d
    curve(4)

    return curve
a=20
f=curve_pre()
print(f.__closure__[3].cell_contents)

# def add():
#     pass
# c=add()
# print(c)

