import random
str = "asdfghjklzxcvbnmqwertyuiop"
list = []
for i in range(1,1001):
    a = random.choice(str)
    list.append(a)
print(list)
zd={}
for j in set(list):
    zd[j]=list.count(j)
print(zd)
li=sorted(zd.items(),key=lambda x:x[1])
li2=dict(li)
print(li2)