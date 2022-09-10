movies = {
    'm1':'sholay' ,
    'm2':'spiderman:no way home',
    'm3':'shrek',
}
print(movies)
print(movies.keys())
print(movies.values())

#traversing a dictionary -> style1 gives only keys
print('style1')
for name in movies :
    print(name)

#traversing a dictionary -> style2 gives only values
print('style2')
for keys in movies:
    print(movies[keys])

#traversing a dictionary -> style3 gives keys and values
print('style3')
for keys in movies:
    print(keys,movies[keys])

#traversing a dictionary -> style3 gives keys and values
print('style4')
for k,v in movies.items():
    print(k,v)


