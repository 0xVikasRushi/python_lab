recursion = lambda n: recursion(n/2) + 1 if n>1 else 1
print(recursion(200))


res = lambda n:res(n/2) +1 if n>1 else 1
print(res(200))