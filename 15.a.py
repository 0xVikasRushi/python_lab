list = [1,2,3,4,5,6,7,8]


def insert(list,position,val):
    if(position<0):
        return '''can't insert'''
    else :
        list.insert(position,val)
        return list

print(insert(list,0,909))