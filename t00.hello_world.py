#!/usr/bin/python3
# x01.hello_world.py

def main():
    print("main")
    init()
    fini()
    
def init():
    print("initialization")

def fini():
    print("finalization")

if __name__ == '__main__':
    main()


