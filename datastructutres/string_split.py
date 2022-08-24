msg =input('enter a sentence :')

words= msg.split()
print(words, len(words), 'words found')

words = msg.split(',')
print(words, len(words), 'words found')

words= msg.split('is')
print(words, len(words), 'words found')

print(msg.split()[-3:])