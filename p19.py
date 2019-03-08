# #水仙花数
#
# for n in range(100,1000):
#
#     i =int( n / 100)
#
#     j =int(n / 10 )% 10
#
#     k =n % 10
#
#     if n == i ** 3 + j ** 3 + k ** 3:
#
#         print(n)

for n in range(100,1000):
    i=int(n/100)
    j=int(n/10)%10
    k=int(n%10)
    if n==i**3+j**3+k**3:
        print(n)