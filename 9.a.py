def f():
    pass
def f2():
    pass
def f3():
    pass
def f4(fun):
    print(id(fun))
test = (f,f2,f3)
for i in test:
    print(i)
    f4(i)