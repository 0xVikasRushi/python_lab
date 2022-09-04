def fib(n):
    a,b=0,1
    while a<n:
        yield b
        a,b=b,a+b
for i in a:
    print(i)