#!/usr/bin/python3

def main():
    print("Generator function .")
    for i in generator(3, 8, 2):
        print(i, end=' ')
def generator(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('Need at least one argument to be passed')
    elif numargs == 1:
        start = 0
        step = 1
        stop = args[0]
    elif numargs == 2:
        (start, stop)= args
        step=1
    elif numargs == 3:
        (start, stop, step)= args
    else:
        raise TypeError("Got more arguments than needed. Got {} arguments".format(numargs))
    while(start<=stop):
        yield start
        start += step
if __name__ == "__main__": main()
