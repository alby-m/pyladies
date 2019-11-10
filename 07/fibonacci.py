
def fibonacci(a,b):
    if b > 100:
        return
    print(a)
    fibonacci(b, a+b)
 
print(fibonacci(0,1))

def fib_iter(n):
    pref = 0
    next = 1
    for i in range(n):
        print(pref)
        tmp = pref     
        pref = next
        next = tmp + pref


fib_iter(20)