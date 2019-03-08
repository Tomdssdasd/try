#对这段文字中的单词进行数字统计，并且进行个数升序
#（能够生成字典8分，字典中统计数正确7分，进行排序8分，最后实现结果7分）

s="The column above illustrates apparently the polularity of people doing exercise in a certain year from 2013 to 2018 Based upon the data we can see that python is wonderful python is wonderful Python"
sp=s.split()
print(sp)
zd={}
for i in set(sp):
    zd[i]=sp.count(i)
print(zd)
li=sorted(zd.items(),key=lambda x:x[1])
li2=dict(li)
print(li2)