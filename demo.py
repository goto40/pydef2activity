
def bar():
    print ("BAR")

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
	for a in range(10):
        	print(a+x*y)
    elif(x==y):
        y=y-1
        print(x+y)        
    else:
        print(y)
    return x+y
