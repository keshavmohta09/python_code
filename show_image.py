from PIL import Image

img = Image.open("wallpaper.jpg")
width, height = img.size
print("Width = ",width,"\nHeight = ",height)
img.show()