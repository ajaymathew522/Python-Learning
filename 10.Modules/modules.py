#!/usr/bin/python3
import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    """import os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    import urllib.request
    page = urllib.request.urlopen('http://bw.org/')
    for r in page:
        print(str(r, encoding='utf_8'), end='')
    
    import random
    x=list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    """
    import  datetime
    now = datetime.datetime.now()
    print(now)
if __name__ == "__main__": main()
