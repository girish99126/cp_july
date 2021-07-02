def pickingNumbers(a):
    a.sort()
    abd=[]
    for i in range(1,len(a)):
        k=[]
        k.append(a[i-1])
        for j in range(i,len(a)):
            if(abs(a[i-1]-a[j]) <=1):
                k.append(a[j])
        abd.append(k)
    
    max=1
    for i in abd:
        if(len(i) > max):
            max=len(i)
    
    return ma