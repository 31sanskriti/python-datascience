#chr= convert integer to string char
x = chr(65)
print(x)

x= chr(2365)
print(x)

x= chr(123465)
print(x)

#ord convert a char to int
y= ord('A')
print(y)

y= ord ('a')
print(y)

y=ord('{')
print(y)

#adding space b/w string 
w1= "this"
w2 = "is"
w3 = "amazing"
msg = w1 +' ' + w2 + ' '+ w3
print(msg)

#duplication 
word= 'Hi'
print(word * 3)
print('_' * 25)

#pattern printing
for i in range (1,6):
    print(i * '☺')

for i in range (6,0,-1):
    print(i * '♣')    

#right aligment
for i in range (1,6):
    print((i * 'V').ljust(15))
    print((i * 'V').rjust(15))


for i in range (1,15,2):
    print((i * 'T').center(50))


for i in range (1,15,2):
    print((i * '♠').center(180))
    print((i * '♦').center(179))

name = 'vijay deenath chauhan'
fname= name[:5]
lname = name[-7:]
mname= name[6:-8]
print(fname,mname,mname)
#reverse
rev_name= name [::-1]
print(rev_name)
#middle name reversed
mname_rev = name[6:-8][::-1]
print(mname_rev) 

#every even index chara
even_name=name[::2]
#every odd index chara
odd_name= name[1::2]
print(even_name , odd_name)     

  

  