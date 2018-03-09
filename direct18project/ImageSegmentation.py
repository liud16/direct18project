# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 12:20:10 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import segmentation
import cv2


def convert_to_grayscale(image):
    
    """Converting the image to grayscale - 
    where minimum pixel value is 0.0 and maximum pixel value is 1.0"""
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # converting to grayscale
    dst = np.zeros(image.shape)
    image_gray = cv2.normalize(image, dst, 0.0, 1.0, cv2.NORM_MINMAX)
    
    # plotting the image
    plt.figure()
    plt.gray()
    plt.title('After background correction, grey-scale')
    plt.imshow(image_gray)
    plt.colorbar()
    
    return image_gray


def seg_random_walker(image, marker_threshold):
    
    """Image segmentation into two regions using skimage random walker segmentation algorithm.
    Input image must be gray scale. This function will provide segmented image and marker positions
    as the output."""
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong image data type', 'image must be a numpy array')
    
    # Checking that the input image is grayscale and not RGB or something else
    assert np.max(image) == 1.0 or 1, ('Wrong input image type', 'image must be grayscale')
    
    assert np.min(image) == 0.0 or 0, ('Wrong input image type', 'image must be grayscale')
    
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

       
    return seg_image
 

def seg(bckgrnd_corr_image):
    """Perform and optimize segmentation of the image"""
    
    seg_ok = 'N'
    while seg_ok == 'N':
        print ('Please choose a threshold for segmentation from 0.0 to 1.0')
        default_threshold = input('Default dimensions? Y/N')    
            
        if default_threshold == 'Y':            
            threshold = 0.15
    
        else:
            threshold = input('Threshold (0.0 to 1.0): ')
        
        image_segmentation = seg_random_walker(bckgrnd_corr_image, threshold)
        
        seg_ok = input('Are you okay with the segmentation?')
    
    return image_segmentation



