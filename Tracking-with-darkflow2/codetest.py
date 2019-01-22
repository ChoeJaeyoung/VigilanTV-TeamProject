dict = {}
dict['가'] = [1,2,3,4]
dict['나'] = [5,6,7,8]
for id, xy in dict.items():
    x1 = xy[0]
    y1 = xy[1]
    x2 = xy[2]
    y2 = xy[3]

print(x1,y1,x2,y2)
print(dict)



#IDcount = {}
#i = 1
#strID = str(i)
#IDcount = {strID : 0, '안녕' : 0, '왜' : 0}
#print(IDcount)

#if strID in IDcount.keys() :
#    IDcount[strID] += 1
#else:
#    IDcount[strID] = 1

#print(IDcount)
#for id_idx, fps in IDcount.items():
#    if fps >= 1:
#        print(id_idx + "입니다")
#print(IDcount.values())




#import numpy as np
#arr = [[1,2,3,3],
#         [4,5,6,6],
#         [7,8,9,9]]

#np.array(arr)
#print(len(arr))

#num = len(arr)
#count = 0
#for i in range(num):
#    print(i)
#    count += 1
#print(count)