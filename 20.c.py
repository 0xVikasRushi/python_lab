f1 = open('inputfile.txt','r')
f2 = open('outputfile.txt','r')
f3 = open('merge.txt','w')
data1  = f1.readlines()
data2  = f2.readlines()
total = data1 + data2
f3.writelines(total)
