def word_counter(s):
    words = s.split()
    return len(words)

def area (l,b):
    return l*b

def circumference(r):
    return 2*3.14*r

print(word_counter('this is an example'))
print(word_counter('welcome to the code of python'))
print(word_counter('hello to my world of coding'))

#area 
#1 direct
print (area(10,10))

#2 user input
a = int(input('enter length :'))
b = int(input('enter breadth:'))
out = area(a,b)
print('area =>' , out)

#3 shorter user input 
out= area(int(input('length:')),int(input('breath:')))
print('area =>', out)




