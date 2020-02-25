#!/usr/bin/python3

class inclusive_range:
    def __init__(self, *args):
        num=len(args)
        if num<1:
            raise TypeError("Need at least one argument")
        elif num==1:
            self.stop=args[0]
            self.start=0
            self.step=1
        elif num==2:
            (self.start, self.stop)=args
            self.step=1
        elif num==3:
            (self.start, self.stop, self.step)=args
        else:
            raise TypeError("Too many arguments, only support 3, got {}".format(num))

    def __iter__(self):
        while self.start <= self.stop:
            yield self.start
            self.start += self.step

def main():
    o = inclusive_range()
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
