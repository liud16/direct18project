# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 20:02:09 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def order_disorder_separation(image, percentile, size):
    
    """Seperates the input image into order and disorder regions using percentile_filter from scipy.ndimage.
    This function will also provide parameters such as order-diorder ratio, order percentage, disorder percentage 
    and total percent coverage from the separated images.
    
    Input image must already be segmented from the background. Output of this function will be filtered image,
    original image, image with ordered regions and image with disoredered regions."""
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # Checking the right data type for the percentile
    assert type(percentile) == int, ('Wrong data type', 'percentile must be an integer')
    
    # Checking the right data type for the size
    assert type(size) == int, ('Wrong data type', 'size must be an integer')
    
    # Using percentile filter to filter image into two labels - 0 and 1 
    filt_img = ndimage.percentile_filter(image, percentile, size, mode='reflect')
    
    plt.figure(dpi = 300)
    plt.imshow(filt_img)
    plt.colorbar()
    plt.title('Filtered image', fontsize = 25)
    
    # creating a boolean array of all the labels - True = label == 1 and False = label == 0
    q = filt_img == 1
    
    # creating empty arrays similar to input image
    I_ordered = np.zeros_like(image)
    I_disordered = np.zeros_like(image)
    
    # Assigning values for ordered and disordered regions
    I_ordered[q] = image[q]
    I_disordered[~q] = image[~q]
    
    # Plotting Original, Ordered and Disordered Image
    
    plt.figure(dpi = 300)
    plt.imshow(image)
    plt.title('Original segmented image', fontsize = 25)
    
    plt.figure(dpi = 300)
    plt.imshow(I_ordered)
    plt.colorbar()
    plt.title('Ordered region', fontsize = 25)
    
    plt.figure(dpi = 300)
    plt.imshow(I_disordered)
    plt.colorbar()
    plt.title('Diordered region', fontsize = 25)
    plt.tight_layout()
    
    # Calculating order disorder ratio, percent coverage of ordered, disordered and overall
    Order_Disorder_ratio = np.sum(np.sum(I_ordered)) / np.sum(np.sum(I_disordered))
    
    Percent_ordered =100* (np.sum(np.sum(I_ordered)) / (image.shape[0] * image.shape[1]))
    
    Percent_diordered =100 * (np.sum(np.sum(I_disordered)) / (image.shape[0] * image.shape[1]))
    
    Percent_coverage = Percent_ordered + Percent_diordered
    
    print 'Order-Disorder ratio = %.5f' %(Order_Disorder_ratio)
    print 'Order Percentage = %.5f' %(Percent_ordered)
    print 'Disorder Percentage = %.5f' %(Percent_diordered)
    print 'Coverage Percentage = %.5f' %(Percent_coverage)
    
    return filt_img, I_ordered, I_disordered