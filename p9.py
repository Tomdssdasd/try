#电脑随机生成1~100随机数，用户输入一个数字，
# 电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
import random
num=random.randint(1,101)
# class range:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         return None
class range:
    def __iter__(self):
        return self
    def __next__(self):
        return None
while 1==1:
    nums=int(input("输入一个数字:"))
    if nums==num:
        print("猜对了")
        break
    elif nums>num:
        print("猜大了")
    elif nums<num:
        print("猜小了")
    else:
        print("猜错了")

