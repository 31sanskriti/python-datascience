def area ():
    l = int(input('enter the length:'))
    b = int(input('enter the length:'))
    return l*b
#calling 
print ("area =>", area())

ans = area()
print('area=>', ans)

ans= area()+ area() -area()
print('total area=>', ans )
 
def minmax():
    x =[23,3,4,5,1,2,3,31,3,5]
    return min(x),max(x)

value = minmax()
x , y = minmax()

print(value)
print(x,y)
print(minmax())

    
 

