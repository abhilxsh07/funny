def f():
    global c
    print("Hello World!", c)
    c+=1
    try:
        f()
    except RecursionError:
        f()
c = 0
f()
