#1.	编写一个八维月考成绩转换函数，输入的成绩是同学在月考中获得的标准成绩，
# 成绩范围0~100。输出的成绩是ABCDE五档。其中，100——90输出A，
# 89——80输出B，79——70输出C，69——60输出D，60分以下的输出E？（
# 15分：分支正确7分，输入、输出正确各4分）

# score=int(input("请输入成绩:"))
# if (score<=100)and(score>=90):
#     print("A")
# elif (score<=89)and(score>=80):
#     print("B")
# elif (score<=79)and(score>=70):
#     print("C")
# elif (score<=69)and(score>=60):
#     print("D")
# else:
#     print("E")

score=int(input("请输入成绩:"))
list=[89,79,69,59]

l=['A','B','C','D']

for i in range(len(list)):
    if score>list[i]:
        print(l[i])
        break
else:
    print("E")