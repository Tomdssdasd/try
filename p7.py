# 输入一个数求1！+2！+3！+4！+n！=？
num=int(input("请输入一个数字:"))
l=1
sum=0
if num<0:
    print("负数没有阶乘")
elif num==0:
    print("0的阶乘为1")
else:
    for i in range(1,num+1):
        l=l*i
        sum+=l
    print("得数是:",sum)