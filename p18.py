# #完全数
# a=range(1,1001)
# b=range(1,1001)
# result=[]
# for i in a:
#     tmp=[]
#     for k in b:
#         if k<i:
#             if not i%k:
#                 tmp.append(k)
#             else:
#                 continue
#         else:
#             break
#     count=sum(tmp)
#     if count==i:
#         result.append(i)
#     else:
#         continue
# print(result)
zd = {}
zd2={}
import random
for i in range(0,100):
    shu=random.randint(0,10)
    if shu > 0:
        zd["正数"+str(i)] = shu
    else:
        zd2["负数"+str(i)] = shu

zd=sorted(zd.items(),key=lambda x:x[1])
print(zd)
print(zd2)