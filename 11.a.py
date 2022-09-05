import random
number= [1,2,3,4,5,6,7,8,9,10,11,12,13]
list = ['heart','spades','diamond','club']
for i in range(0,4):
    num = random.choice(number)
    print(list[i],end=' ')
    print('of',end=' ')
    print(num)
#
