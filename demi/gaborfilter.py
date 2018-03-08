#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:32:11 2018

@author: demiliu
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology, color, segmentation, feature, filters, io
from sklearn import cluster
import cv2
import imagesegregation as IS
import ImagePreprocessing as IP

from skimage.filters import gabor_kernel, gabor
from numpy.linalg import svd

I1 = np.loadtxt('tdj_grbp5_1um_1hr_3rd_020717.001.txt')
#plt.figure()
#plt.title('raw data')
#plt.imshow(I1, cmap = 'gray', interpolation = 'nearest')
#plt.colorbar()

I2 = IP.bckgrnd_correc_sq(I1, 50)
I3 = IP.convert_to_grayscale(I2)
 

gk = gabor(I3, frequency=0.2)
plt.figure()        
plt.imshow(gk[1])  
 


rows = np.shape(I3)[0]
columns = np.shape(I3)[1]

num_points = rows * columns

#wavelengthMin = 4/sqrt(2);
#wavelengthMax = hypot(numRows,numCols);
#n = floor(log2(wavelengthMax/wavelengthMin));
#wavelength = 2.^(0:(n-2)) * wavelengthMin;
#
#deltaTheta = 45;
#orientation = 0:deltaTheta:(180-deltaTheta);
#
#g = gabor(wavelength,orientation);
#gabormag = imgaborfilt(I1_flat_rescaled,g);
#for i = 1:length(g)
#    sigma = 0.5*g(i).Wavelength;
#    K = 1.5;
#    gabormag(:,:,i) = imgaussfilt(gabormag(:,:,i),K*sigma); 

wavelength_min = 20 / np.sqrt(2)
wavelength_max = np.sqrt(rows**2 + columns**2)
n = int(np.log2(wavelength_max / wavelength_min))
n_array = np.arange(0, n-1, 1)

wavelength = np.empty(n-1)
for i in range(n-1):
    
    wavelength[i] = (2 ** n_array[i]) * wavelength_min


deltatheta = 45 / 180
orientation = np.arange(0, 1, deltatheta)

wavelength = wavelength[0:2]
orientation = orientation[0:4]
num_orientation = len(orientation)
num_wavelength = len(wavelength)
num_filter = num_orientation * num_wavelength
g = np.empty((rows, columns, num_filter))

frequency = 1 / wavelength


for f in range(num_filter):
    for j in range(num_orientation):
        for i in range(num_wavelength):
            
            g[:, :, f] = gabor(I3, frequency = frequency[i], theta = orientation[j])[0]

#x = np.arange(1, rows+1, 1)
#y = np.arange(1, columns+1, 1)
#
#X, Y = np.meshgrid(x, y)
#
#g_concate = np.empty((np.shape(g)[0], np.shape(g)[1], np.shape(g)[2]+2))
#g_concate[:, :, -2] = X
#g_concate[:, :, -1] = Y
#g_concate[:, :, :-2] = g
#
#g_reshape = np.empty((num_points, np.shape(g)[2]+2))
#for i in range(num_filter):
#    g_reshape[:, i] = np.reshape(g_concate[:, :, i], num_points)
#
g_reshape = np.empty((num_points, np.shape(g)[2]))
for i in range(num_filter):
    g_reshape[:, i] = np.reshape(g[:, :, i], num_points)


g_standard = (g_reshape - np.mean(g_reshape, axis = 0)) / np.std(g_reshape, axis = 0)

np.savetxt('g_standard.txt', g_standard, fmt='%.5f', delimiter='\t')
