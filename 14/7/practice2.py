x=100
def fun1():
    print(x)

def fun2():
    print(x+10) 

def fun3():
    x=16
    print(x)

def fun4():
    global x
    x=5
    print(x)

def fun5():
    print(x)


fun1()
fun2()
fun3()
fun4()
fun5()
