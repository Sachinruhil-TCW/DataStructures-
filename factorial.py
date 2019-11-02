def getfact(n):
    if n<0:
        return (print("give a positive value"))
    if not n:
        return 
    if n ==1 :
        return 1
    else:
        return n * getfact(n-1)

print(getfact(-3))



def fib(n):
    if n == 1:
        return 1
    if n ==2:
        return 1
    else:
        return  fib(n-1)+fib(n-2)
