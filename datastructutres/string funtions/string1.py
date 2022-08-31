#accessing string characters in python 

str = 'digipodium'
print('str=',str)

#first character
print('str[0]=',str[0])

#second chara
print('str[1]=',str[1])

#last chara
print('str[-1]=',str[-1])

#second last chara
print('str[-2]=',str[-2])


#getting a slice
s = 'digipodium'
slice1 = s[4:7]
slice2 = s[:4]
slice3 = s[0:4]
slice4 = s[4:]
slice5 = s[3:len(s)]
print(slice1)
print(slice2)
print(slice3)
print(slice4)
print(slice5)


