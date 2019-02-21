l=[]
for i in range(1,11):
    import random
    num=random.randint(1,11)
    l.append(num)
    l.sort()
    l.reverse()
print(l)