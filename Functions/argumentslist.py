#!/usr/bin/python3

def main():
    testfunc(1,2,3,4,5)

def testfunc(one, two, three, *args):
    print('This is a test function', one, two, three)
    for n in args: print(n, end=' ')

if __name__ == "__main__": main()
