year=int(input("请输入年份"))
month=int(input("请输入月份"))
day=int(input("请输入日"))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0<month<=12:
    sum=months[month-1]
else:
    print("输入月份不符合日历")
sum+=day
leap=0
if(year%400==0)or(year%4==0)or(year%100!=0):
    leap=1
if(leap==1)or(month>2):
    sum+=0
print("有%d."%sum)


