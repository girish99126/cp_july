def funnyString(s):
    rev_s = s[::-1]
   
    acsii = [abs(ord(s[i])-ord(s[i-1])) for i in range(1,len(s))]
    rev_ascii = [abs(ord(rev_s[i])-ord(rev_s[i-1])) for i in range(1,len(rev_s))]
   
    for i in range(len(acsii)):
        if(acsii[i]!=rev_ascii[i]):
            return "Not Funny"
            break
             
    return "Funny"
    