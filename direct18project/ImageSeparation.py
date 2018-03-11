# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 20:02:09 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def order_disorder_separation(image, percentile, size):
    
    """Seperates the input image into order and disorder regions 
    using percentile_filter from scipy.ndimage.
    This function will also provide parameters 
    such as order-diorder ratio, order percentage, disorder percentage 
    and total percent coverage from the separated images.
    
    Input image must already be segmented from the background. 
    Output of this function will be filtered image,
    original image, image with ordered regions and 
    image with disoredered regions."""
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # Checking the right data type for the percentile
    assert type(percentile) == int, ('Wrong data type', 'percentile must be an integer')
    
    assert 0 <= percentile <= 100, ('Out of range', 'Percentile value must be between 0 and 100')    

    # Checking the right data type for the size
    assert type(size) == int, ('Wrong data type', 'size must be an integer')
    
    # Using percentile filter to filter image into two labels - 0 and 1 
    filt_img = ndimage.percentile_filter(image, percentile, size, mode='reflect')
    
    plt.figure()
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
    
    plt.figure()
    plt.imshow(image)
    plt.title('Original segmented image', fontsize = 25)
    
    plt.figure()
    plt.imshow(I_ordered)
    plt.colorbar()
    plt.title('Ordered region', fontsize = 25)
    
    plt.figure()
    plt.imshow(I_disordered)
    plt.colorbar()
    plt.title('Diordered region', fontsize = 25)
    plt.tight_layout()
    
    # Calculating order disorder ratio, percent coverage of ordered, disordered and overall
    order_disorder_ratio = np.sum(np.sum(I_ordered)) / np.sum(np.sum(I_disordered))
    
    percent_ordered =100 * (np.sum(np.sum(I_ordered)) / (image.shape[0] * image.shape[1]))
    
    percent_disordered =100 * (np.sum(np.sum(I_disordered)) / (image.shape[0] * image.shape[1]))
    
    percent_coverage = percent_ordered + percent_disordered

    print ('--- Disorderness of Image ---')    
    print ('Order-Disorder ratio = %.5f' %(order_disorder_ratio))
    print ('Order Percentage = %.5f' %(percent_ordered))
    print ('Disorder Percentage = %.5f' %(percent_disordered))
    print ('Coverage Percentage = %.5f' %(percent_coverage))
    
    return filt_img, I_ordered, I_disordered, order_disorder_ratio, percent_ordered, percent_disordered, percent_coverage 


def sep(segmented_image):
    """Perform and optimize segmentation of the image"""
    
    sep_ok = 'N'
    while sep_ok == 'N':
        print ('Please enter the parameters for image separation')
        default_parameter = input('Default parameters? Y/N')    
            
        if default_parameter == 'Y':            
            percentile = 30
            size = 10
    
        else:
            percentile = input('Percentile (0 to 100): ')
            size = input('size (integer): ')
        
        image_separation = order_disorder_separation(segmented_image, percentile, size)
        
        sep_ok = input('Are you okay with the separation?')
    
    return image_separation
