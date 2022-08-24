msg ='hello world I am here this is my new file '

count= msg.count('a')
print("a :", count)
count= msg.count('e')
print("e :", count)
count= msg.count('i')
print("i:", count)
count= msg.count('o')
print("o :", count)
count= msg.count('u')
print("u :", count)

for vowels in 'aeiou':
    print(vowels , msg.lower().count(vowels))