#!/usr/bin/python3

def main():
    try:
        fh = open('xlines.txt')
        for line in fh: print(line.strip())
    except IOError as e:
        print("Couldn't open file",e)

if __name__ == "__main__": main()
