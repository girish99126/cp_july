
n = int(input())
lis = list(map(int,input().split()))

avg = sum(lis)
avg=avg/n

print(avg)
melis= lis
melis.sort()

if(n%2!=0):
    x=(n+1)//2
    median=melis[x-1]
    
else:
    y=(n//2)
    median=(melis[y-1]+melis[y])/2
    


print(median)

d={}
for i in lis:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1

mode = max(d, key=d.get)
print(int(mode))
