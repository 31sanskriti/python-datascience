x = [1,2,3,4,5,6,7,8,5]
y = [4,5,6,7,2,3,5,6,9]
o = list (map(lambda i: i**2 , x))
x5 = list(map(lambda i: i-5,x))
xy = list(map(lambda a,b : a+b , x,y))
print(o)
print(x5)
print(xy)

name =['Ajay singh', 'vijay kumar', 'Ravi singh', 'Raj kumar', 'Raja singh',
        'simran kumar','Aparna singh','Reema verma']
name1= list(filter(lambda n: n.endswith('singh'),name))
name2 = list(filter(lambda n: n.startswith('R'),name))
print(name1)
print(name2)
