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
    
    """Image segmentation into two regions using skimage random walker segmentation algorithm.
    Input image must be gray scale. This function will provide segmented image and marker positions
    as the output."""
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong image data type', 'image must be a numpy array')
    
    # Checking that the input image is grayscale and not RGB or something else
    assert np.max(image) == 1.0, ('Wrong input image type', 'image must be grayscale')
    
    assert np.min(image) == 0.0, ('Wrong input image type', 'image must be grayscale')
    
    # Checking the right data type and range for marker threshold value
    assert type(marker_threshold) == float, ('Wrong data type', 'marker threshold must be a float')
    
    assert 0.0 <= marker_threshold <= 1.0, ('Marker threshold out of range', 'Marker threshold must be between 0 and 1')    
    
    # Random walker segmentation    
    markers = np.zeros(image.shape)
    markers[image < marker_threshold] = 1 # ordered regions
    markers[image > marker_threshold] = 2 # disordered regions
    
    # Segmented Image
    segmented = segmentation.random_walker(image, markers)
    
    # Plotting the segemented, original image and markers
    plt.figure(dpi = 300)
    seg_image = convert_to_grayscale(segmented)
    plt.title('Segmented Image')

    plt.figure(dpi = 300)
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.title('Original Image')
    
    plt.figure(dpi = 300)
    plt.imshow(markers, cmap='plasma', interpolation='nearest')
    plt.colorbar()
    plt.title('Markers')

       
    return seg_image
    
