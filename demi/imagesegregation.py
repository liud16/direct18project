#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 13:31:28 2018

@author: demiliu
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 12:20:10 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import segmentation
from sklearn import cluster
from ImagePreprocessing import convert_to_grayscale

def seg_random_walker(image, marker_threshold):
    
    """Image segmentation using skimage random walker segmentation algorithm."""
    
    markers = np.zeros(image.shape)
    markers[image < marker_threshold] = 1 # ordered regions
    markers[image > marker_threshold] = 2 # disordered regions
    
    segmented = segmentation.random_walker(image, markers)
    
    plt.figure()
    seg_image = convert_to_grayscale(segmented)
    plt.title('Segmented Image')

    plt.figure()
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.title('Original Image')
    plt.figure()
    plt.imshow(markers, cmap='plasma', interpolation='nearest')
    plt.colorbar()
    plt.title('Markers')

       
    return segmented
    
