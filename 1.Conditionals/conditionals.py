#!/usr/bin/python3
def main():
  a,b=0,1
  if a<b:
      print("a({}) is less than b({})".format(a,b))
  elif a>b:
      print("a({}) is greater than b({})".format(a,b))
  else:
      print("a({}) is equal to b({})".format(a,b))
if __name__ == "__main__": main()
