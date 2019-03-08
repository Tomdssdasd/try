#生成一个有10个数的随机数组，判断每个数字出现的次数
import random
l=[]
for i in range(0,10):
    shu=random.randint(0,10)
    l.append(shu)
print(l)

zd={}
for i in set(l):
    zd[i]=l.count(i)
print(zd)