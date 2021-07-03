def jumpingOnClouds(c):
    co=0
    i=0
    while i < len(c)-1:
        if(i+2 <len(c) and c[i+2]==0):
            co+=1
            i=i+2
        else:
            co+=1
            i=i+1
    return c