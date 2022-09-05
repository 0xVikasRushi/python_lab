# def toh(n,source,destination,aux):
#     if n==1:
#         print('move disk 1 from source ',source,'to destination', destination)
#         return
#     toh(n-1,source,aux,destination)
#     print('move disk',n,'from source ',source,'to destination',destination)
#     toh(n-1,aux,destination,source)








def toh(n,s,d,a):
    if(n==1):
        print('move disk 1 form sorce',s,'to destination',d)
        return
    toh(n-1,s,a,d)
    print('move disk ',n,'form source', s, 'to destination', d)
    toh(n-1,d,a,s)

toh(4,'a','b','c')