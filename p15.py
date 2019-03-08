#回文字符串

str=input("请输入字符串")
if str[::1]!=str[::-1]:
    print("不是")
else:
    print("是")