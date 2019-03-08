import random
def gee():
    b="ABCD"
    str=""
    for i in range(20):
        s=random.choice(b)
        str+=s
    return str
with open("num.txt","w") as f:
    for i in range(500):
        f.write('S'+str(i+1).zfill(5)+"\t"+gee()+'\n')
