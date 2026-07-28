import imageio.v3 as iio
filenames = ['cola.png', 'cola2.png']
images = []
for filename in filenames:
    image = iio.imread(filename)
    images.append(image)

iio.imwrite('output.gif', images, duration=450,loop=0)
print("GIF created successfully!")