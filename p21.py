name=input("请输入文件名:")
id=input("请输入序列号:")
list=[]
with open("searchResult.txt","w") as f:
    with open(name) as fp:
        data=fp.readlines()
        for i in data:
            if id in i:
                j=i.split("\t")[-1]
                fp.seek(0,0)
                for x in fp.readlines():
                    count=0
                    y=x.split("\t")[-1]
                    for m in range(20):
                        if j[m]==y[m]:
                            count+=1
                    result=x.replace('\n','\tcount='+str(count)+'\n')
                    list.append(result)
        results=sorted(list,key=lambda aStr:int(aStr[aStr.find("=")+1:-1:]))
        results.reverse()
        for mm in results:
            f.write(mm)