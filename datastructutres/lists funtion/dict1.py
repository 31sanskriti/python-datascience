info = ['Mistborn','The final empire','Brandon sanderson','tor.com',2099,2002]

info_dict ={

    'series': 'Mistborn',
    'title' : 'The final empire',
    'author': 'Brandon sanderson',
    'publisher':'tor.com',
    'price':'2099',
    'year':'2002'

    }

print(info_dict)
print(info_dict.keys())
print(info_dict.values())
print(info_dict['title'])
print(info_dict.get('author'))

#update the existing value 
info_dict['price'] =599
print(info_dict)

#adding a new key value pair
info_dict['rating'] = 10
print(info_dict)