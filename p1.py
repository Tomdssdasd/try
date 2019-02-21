l=[]
for i in range(5):
    import random
    list=random.randint(1,10)
    l.append(list)
else:
    print(l)
import random
num=random.randint(1,10)
print(num)
# l.append(num)
# if len(l)!=len(set(l)):
#     print("不存在")
# else:
#     print("存在")
for j in range(5):
    if num==l[j]:
        print("存在")
        break
else:
        print("不存在")

