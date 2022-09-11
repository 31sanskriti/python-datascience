
from PIL import Image

im = Image.open(r'C:\Users\91926\Downloads\pang-yuhao-wCi28eq8TF4-unsplash.jpg') #relative addr
im2 =Image.open(r'C:\Users\91926\Downloads\mohammad-mardani-6VpFnMxhcHs-unsplash.jpg')# absolute addr

print('resolution' , im.size)
print('height' , im.height)
print('width' , im.width)
print('mode' , im.mode)
print('format' , im.format)
print('exif' , im.info)

im.convert('L').show()
im.resize((100,100)).show()
im2.resize((im.width *5 , im.height*5)).save(r'C:\Users\91926\Downloads\mohammad-mardani-6VpFnMxhcHs-unsplash.jpg')
