# -*- coding: utf-8 -*-

import cv2
import numpy as np 
import os
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, spline, CubicSpline
import matplotlib.patches as mpatches


path = os.getcwd()

def main():
	
	images = [f for f in os.listdir(path) if f.endswith('.JPG')]
	data = []

	for i in images:
		j = 0
		img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
		x, y = img.shape[:2]
		img = img[int(y/2)-100:int(y/2)+200, int(x/2)-100:int(x/2)+200]
		cv2.imwrite(path+ '/Test/' + 'n{}'.format(i), img)
		c = np.std(img)
		data.append(c)
		j += 1

	fig = plt.figure()
	xnew = range(0,51)
	norm = max(data)
	new_data = data[:]/norm

	xsmooth = np.linspace(0, 50, num=200, endpoint = True)
	f = interp1d(xnew, new_data)

	plt.plot(new_data, 'o', color = 'red')
	plt.plot(xsmooth, f(xsmooth), '-', color = 'green')

	data_patch = mpatches.Patch(color='red', label='Dane')
	plt.legend(handles = [data_patch])
	plt.title('Kontrast'.encode('utf-8').decode('utf-8'))
	plt.grid(True)
	plt.ylabel('konrast [j.u.]')
	plt.xticks(np.arange(0, 51, 5.0))
	plt.yticks(np.arange(0, 1, 0.1))
	plt.xlabel('d [cm]')
	plt.show()
	fig.savefig('wykres.png')


main()