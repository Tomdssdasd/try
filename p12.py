
# import random
# list = []
# for i in range(1,21):
#     a = random.randint(-10,10)
#     list.append(a)
# print(list)
# ouli = list[0:len(list):2]
# print(ouli)
# ouli.sort(reverse=True)
# print(ouli)
# a = 0
# for i in range(0,len(list)):
#     if i%2==0:
#         list[i] = ouli[a]
#         a+=1
# print(list)
# #编写程序，生成一个包含20个随机整数的列表，
# # 然后对其中偶数下标（下标即列表元素的索引）的元素进行降序排列，奇数下标的元素不变。
# # （提示：使用切片。） (20分：生成列表5分，找到偶数下标8分，降序7分)
import  random
list=[]
for i in range(20):
    shu=random.randint(-10,10)
    list.append(shu)
print(list)
ouli=list[0:len(list):2]
print(ouli)
ouli.sort(reverse=True)
print(ouli)
a=0
for i in range(0,len(list)):
    if i%2==0:
        list[i]=ouli[a]
        a+=1
print(list)