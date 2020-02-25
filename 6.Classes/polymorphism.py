#!/usr/bin/python3

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    def bark(self):
        print("Ducks cannot bark")
    def fur(self):
        print("I have feathers not fur")
class Dog:
    def bark(self):
        print("I bark ")
    def fur(self):
        print("I have brown and white fur")
    def walk(self):
        print("I like to run")
    def quack(self):
        print("I don't quack I bark")
def main():
    donald = Duck()
    jimmy = Dog()
    for i in (donald, jimmy):
        i.bark()
        i.quack()
        i.fur()
        i.walk()
    the_forest(donald)
    the_pond(jimmy)
def the_forest(dog):
    dog.bark()
    dog.fur()
def the_pond(duck):
    duck.quack()
    duck.walk()
if __name__ == "__main__": main()
