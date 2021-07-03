def weightedMean(x, w):
    s=sum([x[i]*w[i] for i in range(len(x))])
    print(round(s/sum(w),1))
   