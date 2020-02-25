#!/usr/bin/python3

def main():
    testfunc(23,"Passing arguments",True)
    print("func() is being called")
    func()
    print("func was called")
    func2("one value")
def testfunc(number, onemore="Nothing was passed", anotherone=False):
    print('This is a test function', number, onemore, anotherone)
def func():
    pass
def func2(str, fun=None):
    print("This is in func2 ", str, fun)
    if fun is  None:
        fun="Value has been assigned to fun"
    print("After conditional check ", str, fun)

if __name__ == "__main__": main()
