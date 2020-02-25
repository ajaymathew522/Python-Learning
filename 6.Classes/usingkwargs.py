#!/usr/bin/python3

class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    def set_variable(self,k,v):
        self.variables[k] = v
    def get_variable(self,k):
        return  self.variables.get(k , None)
def main():
    donald = Duck(name='donald', feet=2)
    donald.quack()
    donald.walk()
    print("Name is", donald.get_variable('name'))
    print("Color is", donald.get_variable('color'))
    print("I have {} feet".format(donald.get_variable('feet')))
    donald.set_variable('color' , 'blue' )
    print("Color is", donald.get_variable('color'))
if __name__ == "__main__": main()
