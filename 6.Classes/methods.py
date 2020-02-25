#!/usr/bin/python3

class Duck:
    def __init__(self, value):
        print("This is the constructor")
        self.v=value
    def quack(self):
        print("I Quacked {} times!".format(self.v))

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck(22)
    joe = Duck(100)
    donald.quack()
    donald.walk()
    joe.quack()
    joe.walk()
if __name__ == "__main__": main()
