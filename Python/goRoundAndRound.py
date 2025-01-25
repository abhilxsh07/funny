#this code's only goal is to recursively call the same function over and over again. a bit memory consuming but the larger goal is to understand how easy it is in large scale applications to make this blunder.

def f():
    global c
    print("Hello World!", c)
    c+=1
    try:
        f()
    except RecursionError: #to prevent code from stopping (inadvertently, for a use case where this function should be running all the time)
        f()
 
#MAIN
c = 0
f()
#press Alt+F4 to exit

