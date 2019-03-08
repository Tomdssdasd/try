#读入文件‘monday.txt’.统计文件中每个单词的数量并且进行输出。
# re=open("monday.txt","r")
# se=re.read(500)
# print(se)
# sp=se.split(" ")
# print(sp)
# zd={}
# for i in set(sp):
#     zd[i]=sp.count(i)
# print(zd)
# li=sorted(zd.items(),key=lambda x:x[1])
# li2=dict(li)
# print(li2)

re=open("monday.txt","r")
se=re.read(500)
print(se)
sp=se.split()
print(sp)

zd={}
for i in set(sp):
    zd[i]=sp.count(i)
print(zd)

li=sorted(zd.items(),key=lambda x:x[1])

li2=dict(li)
print(li2)