# pydef2activity

Small example how to transform a 

## Run

Usage: ```./pydef2activity <file> <function name>```

## Example

Command: ```./pydef2activity demo.py foo```

Input (demo.py)
```
def foo(y=2):
    x=3
    #comment1
    #activity TEST1
    if x>2:
        x=1
        print(y)
    #end activitiy
    print(x*2)
    if(x>y):
        print(x*y)
    elif(x==y):
        y=y-1
        print(x+y)        
    else:
        print(y)
    return x+y
```
Output: ![Example output for demo.py](foo.png?raw=true)

## Install

get the red baron full-AST-parser: ```pip3 install redbaron```
