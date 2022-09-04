import os
f1 = open('empdata.txt','r')
data = f1.readlines()
# for i in data:
words =0
for i in data:
    word = i.split()
    words+=len(word)

print(words)
print(data)