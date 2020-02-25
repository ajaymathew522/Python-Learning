#!/usr/bin/python3

class Animal:
    def talk(self):print("I have something to say!")
    def walk(self):print("I like to walk")
    def clothes(self):print("I have clothes")

class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super(Duck, self).walk()
        print('Walks like a duck.')
class Dog(Animal):
    def clothes(self):print("I have fur")
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    ronald = Dog()
    ronald.walk()
    ronald.clothes()
if __name__ == "__main__": main()
