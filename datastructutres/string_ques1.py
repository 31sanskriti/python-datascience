#question1
#wap to count the alphabets in a string
#and display the output like 
#a-3
#b-9
#.....
#z-0
from string import ascii_lowercase

msg ='life before death , hope before despair'
for char in ascii_lowercase:
    print(f'{char} - {msg.count(char)}')

