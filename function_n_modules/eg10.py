#variable arguments - args
#keywords arguments - kwargs

def total(*values):
    t=0
    for i in values:
        if isinstance(i,(int,float)):
            t +=i

    return t 

o = total(1,2,3,4)
print(o)
o = total()
print(o)
o= total(1,23,45,56,23,43,65,78,90,123,564,768,894)
print(o)
o=total(2,3,42,65,78,98,'a',45,622,'g')
print(o)

