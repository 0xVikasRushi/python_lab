n  = int(input('Enter the n : '))
list = [1,2,3,4,5]
ans = []
list2 = []
for i in range(1,n+1):
    list2 = [i*j for j in list]
    ans.append(list2)
print(ans)