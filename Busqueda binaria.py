import random
from typing import Sized

values = []
for i in range(1,10):
    values.append(random.randint(1, 1000))
values.sort()
print ( values )

def bs(k):
    l=0
    r=len(values)-1

    while (l<=r):
        m = (l+r)/2
        if(k==values[m]):
            return m
        elif(k<values[m]):
            r = m-1
        else:
            l = m+1
    return -1