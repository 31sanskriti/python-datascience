# create a list of n numeric elements
# generate a list of even number from existing list 
# generate a list of odd number from existing list 
# generate a list of only number > x from existing list, where n can be any value
x = [2,4,5,1,6,7,8,9,4,2,5,8,9,28,23,89] 

xe = []
for i in x :
    if i % 2 == 0:
        xe.append(i)
print(x)
print(xe)
xo = []
for i in x :
    if i % 2 != 0:

        xo.append(i)
print(xo)

xg = []
for i in x :
    if i > 20 :
        xg.append(i)
print(xg)
