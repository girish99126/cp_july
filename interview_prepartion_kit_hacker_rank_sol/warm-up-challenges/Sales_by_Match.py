def sockMerchant(n, ar):
    count=0
    l={}
    for i in ar:
        if(i not in l):
            l[i]=1
        else:
            l[i]+=1
    
    for k,v in l.items():
        d=v//2
        if(d >0):
            count+=d
        else:
            continue
    return count
