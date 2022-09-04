#Write programs that exchange the contents of two files.

import os

f1 = open('inputfile.txt','r')
f2 = open('outputfile.txt','r')

data1 = f1.readlines()
data2 = f2.readlines()

f1 = open('inputfile.txt','w')
f2 = open('outputfile.txt','w')

f1.writelines(data2)
f2.writelines(data1)
