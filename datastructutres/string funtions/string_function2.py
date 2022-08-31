#string validation function
value = input('enter something:')

if value.isnumeric():
    print("only number", value.isnumeric())
if value.isalpha():
    print("only alphabets", value.isalpha())   
if value.isalnum():
    print ('alphabets & number', value.isalnum())
if value.isspace():
    print('only space', value.isspace())
if value.isupper():
    print('uppercase alphabets', value.isupper())
if value.islower():
    print('lowercase alphabets', value.islower())
