def maxCount(m, n, ops):
        minx=m
        miny=n
        for x,y in ops:
            minx=min(minx,x)
            miny=min(miny,y)
        return minx*miny
m=3
n=3
l=[]
print(maxCount(m,n,l))

       
