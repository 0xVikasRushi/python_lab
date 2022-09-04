import os
f1 = open('empdata.txt','r')
data = f1.readlines()
cnt=0
for i in data:
    if i =='\n':
        cnt+=1
print(cnt)
