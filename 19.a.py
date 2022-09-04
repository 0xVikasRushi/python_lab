def reverse(String):
    for i in range(len(String)-1,-1,-1):
        yield String[i]
for i in reverse('vikas'):
    print(i,end='')