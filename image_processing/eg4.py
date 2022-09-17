from PIL import Image , ImageFont , ImageDraw

im = Image.open(r'C:\Users\91926\Downloads\pang-yuhao-wCi28eq8TF4-unsplash.jpg') #relative addr
im2 =Image.open(r'C:\Users\91926\Downloads\mohammad-mardani-6VpFnMxhcHs-unsplash.jpg')# absolute addr

font = ImageFont.truetype(r'C:\Windows\Fonts\IMPRISHA.TTF',200) 
#truetype is used to give font address which is ttf 
font2 = ImageFont.truetype(r'C:\Windows\Fonts\VLADIMIR.TTF' ,250)


imd = ImageDraw.Draw(im)
imd.text((200,200),'ASTHECTIC',fill=(250,250,250),font=font,)
imd.text((500,500),'BY-sanskriti',fill=(250,250,250),font=font2)
im.show()