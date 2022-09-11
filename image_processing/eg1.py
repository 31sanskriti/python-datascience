
from PIL import Image

im = Image.open(r'C:\Users\91926\Downloads\pang-yuhao-wCi28eq8TF4-unsplash.jpg') #relative addr
im2 =Image.open(r'C:\Users\91926\Downloads\mohammad-mardani-6VpFnMxhcHs-unsplash.jpg')# absolute addr

print(im)
print(im2)

im.rotate(45).show()

im2.rotate(90).show()

 