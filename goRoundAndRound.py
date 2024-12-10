def f():
    print("Hello World!")
    try:
        f()
    except RecursionError:
        f()
f()