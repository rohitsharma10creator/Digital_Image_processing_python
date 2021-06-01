from PIL import Image, ImageOps
im1 = Image.open(r"C:\Users\admin\Desktop\kuva\kuva.png")
im2 = ImageOps.grayscale(im1)
im2.show()

