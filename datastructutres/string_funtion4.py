#strings endswith


file = input('enter file name:')

if file.endswith('.png'):
    print('its a png file')
elif file.endswith('jpg'):
    print('its a jpg file')
elif file.endswith('docx'):
    print('its a word file')
elif file.endswith('.py') or file.endswith('.ipynb'):
    print('its a python file')
else:
    print('un identified file,destroy your computer')
