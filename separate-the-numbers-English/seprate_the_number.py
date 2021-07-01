
def separateNumbers(s):
    possible=[]
    if(len(s)==1):
        print("NO")
    else:
        for i in range(1,len(s)//2+1):
            genstr = s[:i]
            print(genstr)
            prev = int(genstr)
            print(prev)
            while len(genstr)<len(s):
                next = prev+1
                print(next)
                genstr = genstr+str(next)
                print(genstr)
                prev=next
            if genstr == s:
                print("YES",s[:i])
                return
        print("NO")