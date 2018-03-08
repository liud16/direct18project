#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:55:53 2018

@author: demiliu
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology, color, segmentation, feature, filters, io
from sklearn import cluster
import cv2

from sklearn.cluster import KMeans
from skimage.filters import gabor_kernel, gabor
from numpy.linalg import svd

g_standard = np.genfromtxt('g_standard.txt', delimiter = '\t')

km = KMeans(n_clusters = 2)
g_fit = km.fit_predict(g_standard)

g_fit_reshape = np.reshape(g_fit, (512, 512))

plt.imshow(g_fit_reshape)