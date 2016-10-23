from scipy import misc

image = misc.imread("image.bmp")

# dimension, number of channels
print img.shape

# range of pixel shades
print img.dtype

# scale colors to 0-1
img = (img / 256.0)

#reshape
img = img.reshape(-1, 3)

# luminance 
red = img[:,0]
green = img[:,1]
blue = img[:,2]

grayscale = (0.299*red + 0.587*green + 0.114*blue)

# 3 channels
print img.shape

# 1 channels
print grayscale.shape