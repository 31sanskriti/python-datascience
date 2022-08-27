#question 2
#wap to remove all the punctuations from the string

from string import punctuation

msg= '/this is that and that is this, !that is that,and this is this'

for p in punctuation:
    msg = msg.replace(p,'')
print(msg)


