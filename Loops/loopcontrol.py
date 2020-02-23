#!/usr/bin/python3
def main():
    s = 'this is a string'
    for c in s:
        if c=='s': continue
        print(c, end='')
    print()
    for c in s:
        if c=='s': break
        print(c, end='')
    print()
    for c in s:
        print(c, end='')
    else:
        print('else')

if __name__ == "__main__": main()
