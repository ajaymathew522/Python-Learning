#!/usr/bin/python3

def main():
    testfunc(1, 2, 3, 4, 5, 6, one='test1', two=23, three= True)

def testfunc(a, b, c, *args, **kwargs):
    print('This is a test function',a, b, c, args,
          kwargs['one'], kwargs['two'], kwargs['three'])
    print(kwargs)
    for k in kwargs:print(k, kwargs[k])
    for i in args: print(i, end=' ')


if __name__ == "__main__": main()
