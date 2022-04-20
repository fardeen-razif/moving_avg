import random

i=0

while i<10:
    a=random.random()
    l=[]
    l.append(a)
    q=len(l)
    avg=0

    if q<5: 
        avg=sum(l)/q
        print(avg)

    else :
        avg=(l[q-1]+l[q-2]+l[q-3]+l[q-4]+l[q-5])/5
        print(avg)

    i=i+1    
    # could have made this into an infinte loop as well 














