#.有一列分数序列，2／1，3／2，5／3，8／5。。。求出前20项之和
a=2
b=1
sum=0
for i in range(1,21):
    sum+=a/b
    t=a
    a=a+b
    b=t
print("和是:%.2f"%sum)