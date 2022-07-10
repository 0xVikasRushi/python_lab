
rows  =int(input("Enter the number of rows : "))

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Upper part
for i in range(0,rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print()

# Lower Part
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()
