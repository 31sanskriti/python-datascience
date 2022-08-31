#create a list with 10 numeric values from user
#then find the min , max, total,avg,median


import statistics as stat

x = []
for i in range (1,11):
    val =int(input(f'enter the value{i} ->'))
    x.append(val)

for i in x:
    print(i , end='')

print("minimum value:" , min(x))
print("maximum value:" , max(x))
print("total of values:" ,sum(x))
print("average of values:" ,stat.mean(x))
print("mediam of values:" , stat.median(x))
