#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os

""" Returns a list of filenames for all jpg images in directory """
def get_imList(path):
	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

""" Open and convert image to another format """
try:
	pil_img = Image.open('lena.jpg')
	#pil_img.save('lena.bmp')
except IOError:
	print "cannot convert"
	
""" Create thumbnail """
#pil_img.thumbnail((64,64))

""" Resize and rotate """
out = pil_img.resize((128,128))
out = pil_img.rotate(45)
out.save('lena.bmp')