from PIL import Image

img = Image.open("0eda13921425483.png")
img = img.resize((8,8), Image.ANTIALIAS)
img.save("mooshroom.png", dpi=(8,8))
