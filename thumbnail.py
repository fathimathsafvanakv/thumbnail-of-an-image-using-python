#importing image fom pil library
from PIL import Image
#created an object image
image=Image.open("E:\wallpapers\wallpaper.jpg")
maximum_size=(100,100)
image.thumbnail(maximum_size)
#ceating thumbnail
image.show()
image.save("thumbnailofwallpaper.png")