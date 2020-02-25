#!/usr/bin/python3
def main():
    print("This is the functions.py file.")
    for i in iterator(1, 25, 3):
        print(i, end = ' ')
def iterator(start=0, stop, step=1):
    i=start
    while(i<=stop):
        yield i
        i+=step

if __name__ == "__main__": main()
