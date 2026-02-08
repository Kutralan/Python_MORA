def factorial(inp):
    

    factorial=1
    while inp>1:
        k=inp
        h=k*(inp-1)
        factorial=factorial*h
        inp=inp-2

    return factorial

inp=int(input("enter a non-negative integer: "))
print(factorial(inp))



