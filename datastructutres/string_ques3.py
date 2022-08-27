#question 3
#wap to find all the occurance of a word in a string and display its index

msg= 'this is that and that is this, that is that and this is this'

start =0
query = 'that'
while True:
    idx = msg.find(query , start)
    if idx == -1:
        break
    print(f'{query} at {idx}')
    start = idx + 1

