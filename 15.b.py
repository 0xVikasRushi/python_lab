import functools
list  = [1,2,3,4,5,6,7]


a  = functools.reduce(lambda a,b:a+b,list)
print(a)
