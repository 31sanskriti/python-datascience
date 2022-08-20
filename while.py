x = 1 
while x<7:
    print('num')
    x +=1
print('stop')

for i in range(1,11):
    if(i==7):
        print('out of loop')
        break
    else:
        print(i)

for i in range(1,11):
    if(i==7):
        continue
    else:
        print(i)