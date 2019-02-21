import random
str = "asdfghjklzxcvbnmqwertyuiop"
list = []
for i in range(1,1001):
    a = random.choice(str)
    list.append(a)
print(list)
sett = set(list)
cs = []
for i in range(0,len(sett)):
    a = list.count(sett.pop())
    cs.append(a)
zm = set(list)



jh = {}
for i in range(0,len(zm)):
    jh[zm.pop()] = cs[i]
print(jh)