from PIL import Image, ImageFilter , ImageEnhance 

im = Image.open(r'C:\Users\91926\Downloads\pang-yuhao-wCi28eq8TF4-unsplash.jpg') #relative addr
im2 =Image.open(r'C:\Users\91926\Downloads\mohammad-mardani-6VpFnMxhcHs-unsplash.jpg')# absolute addr

#im.filter(ImageFilter.EMBOSS).show()
#im.filter(ImageFilter.CONTOUR).show()
#im.filter(ImageFilter.FIND_EDGES).show()
#im.filter(ImageFilter.BLUR).show()
#im.filter(ImageFilter.SHARPEN).show()
#im.filter(ImageFilter.SMOOTH).show()
#im.filter(ImageFilter.MaxFilter(5)).show() #highlight whites
#im.filter(ImageFilter.MinFilter(5)).show()  #highlight blacks
#im.filter(ImageFilter.MedianFilter(8)).show() #highlight greys 
#im.filter(ImageFilter.GaussianBlur(8)).show()

eim = ImageEnhance.Color(im)
for i in range(-10,11,2):
    eim.enhance(i).show()

imc = im.copy()
im2_s = im2.resize((1000,1000))
imc.paste(im2_s ,(700,0))
imc.show()

