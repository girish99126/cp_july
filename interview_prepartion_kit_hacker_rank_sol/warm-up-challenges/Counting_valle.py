# Complete the countingValleys function below.
def countingValleys(n, s):
    l=[]
    for i in range(len(s)):
        l.append(s[i])
    v=0
    lev=0
    for i in l:
        if(i=="U"):
            lev+=1
        elif(i=="D"):
            lev-=1
        
        if(lev==0 and i=="U"):
            v+=1
    return v
        