from PIL import Image
im = Image.open("tilin.jpeg")

print(im.format, im.size, im.mode)

box = (0, 0, 400, 400)
region = im.crop(box)
region.save("recorte.png")

r, g, b = im.split()
im = Image.merge("RGB", (r, g, b))
region.save("tilinexe.png")

out = region.rotate(45)
out.save("giro.png")