month1=int(input("请输入第一个人的月份"))
month2=int(input("请输入第二个人的月份"))
if month1>month2:
    month3=month1%month2
    if month3==1:
        print("非常有缘")
    elif month3==2:
        print("比较有缘")
    elif month3==3:
        print("缘分一般")
    elif month3==4:
        print("仇人")
    else:
        print("无缘")
else:
    month3 = month2 % month1
    if month3 == 1:
        print("非常有缘")
    elif month3 == 2:
        print("比较有缘")
    elif month3 == 3:
        print("缘分一般")
    elif month3 == 4:
        print("仇人")
    else:
        print("无缘")
