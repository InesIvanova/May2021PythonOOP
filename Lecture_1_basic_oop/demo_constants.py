def outer1():
    x = 20
    def outer2(): 
        x = 10
        def inner():
            nonlocal x
            x = 5

        inner()
        print(x)
    outer2()
    print(x)

outer1()
