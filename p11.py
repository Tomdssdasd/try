#编写程序，生成一个包含50个随机整数的列表，
# 随机整数的范围是从-10到10，然后将列表中所有的正
# 数存为一个新的子列表，负数存为另一个新的子列表。（
# 15分：生成随机列表5分，得出正负数新列表各5分）
l=[]
d=[]
for i in range(50):
    import random
    num=random.randint(-10,10)
    if num>0:
        l.append(num)
    elif num<0:
        d.append(num)
print(l)
print(d)