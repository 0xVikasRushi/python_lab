import os,filecmp
f1 = 'inputfile.txt'
f2 = 'outputfile.txt'
# result shallow mode
# filecmp.cmp(filepath,filepath)
res = filecmp.cmp(f1,f2)
deep = filecmp.cmp(f1,f2,shallow=False)
print(res)
print(deep)