def gemstones(arr):
    fre={}
    j = ("").join(arr)
    j=list(set(j))
    for i in range(len(j)):
        fre[j[i]]=[]   
    for i in range(len(arr)):
        for j in arr[i]:
            if(j in fre):
                s=fre[j]
                s.append(i)
                fre[j]=s
    res=[i for i in range(len(arr))]
    s= list(fre.values())
    c=0
    for i in range(len(s)):
        check =  all(item in s[i] for item in res)
       
        if(check):
            print(s[i],res)
            c+=1
    return c
