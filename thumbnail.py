from PIL import Image
image=Image.open("E:\wallpapers\wallpaper.jpg")
maximum_size=(100,100)
image.thumbnail(maximum_size)
image.show()
image.save("thumbnailofwallpaper.png")