from PIL import Image, ImageDraw, ImageFont
 
img = Image.new('RGB', (108, 108), color = (255,255,255))

ft = 'fonts\\BELL.ttf'

c = 'a'

fnt = ImageFont.truetype(ft, 150)
d = ImageDraw.Draw(img)
d.text((10,-42), c, font=fnt, fill=(0,0,0))
 
img.save('pil_text.png')