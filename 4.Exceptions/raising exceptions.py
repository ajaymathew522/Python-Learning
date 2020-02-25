#!/usr/bin/python3

def main():
    try:
        for line in readfile('xlines.docx'): print(line.strip())
    except IOError as e:
        print("Couldn't open file:",e)
    except ValueError as e:
        print('bad file name',e)
def readfile(filename):
    if filename.endswith('.txt'):
        fh=open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
if __name__ == "__main__": main()
