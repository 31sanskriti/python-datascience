#question -1
#wap to create a list from user of n elements. if a users enters a duplicate value 
#don't add it to list and warn the user about there mistake  

l = []
while True:
    Number = input("Please enter a number: ")
    if Number not in l:
        Number = l.append(Number)
        print(l)
    else:
        print(f'{Number} Already exist in your list .')

