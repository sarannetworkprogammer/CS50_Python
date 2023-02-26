from PIL import Image, ImageOps

image1 = Image.open(sys.argv[1])


shirt = Image.open("shirt.png")

size = shirt.size

image1 = ImageOps.fit(image1, size)

image1.paste(shirt, shirt)

image1.save(sys.argv[2])