import os
# # opening  files
# # objectname = open(filepath,mode)
# # f1 = open('open.txt','r')
#
# ## for text files we use r
# # for binary files we use rb
# f1 = open('input.txt','r')
# a = f1.read()
# print(a)
#

# f2  = open('outputfile.txt','w')
# with open('inputfile.txt','r') as file:
# 	data = file.readlines()
# changingdata = data[::-1]
#
# f2.writelines(changingdata)
# f2.close()














f2  = open('outputfile.txt','w')
with open('inputfile.txt','r') as file:
    data = file.readlines()
newdata = data[::-1]
f2.writelines(newdata)
f2.close()