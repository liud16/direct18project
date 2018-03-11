#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 08:56:28 2018

@author: demiliu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import morphology
import cv2
from skimage import segmentation
from sklearn import cluster
from ImagePreprocessing import convert_to_grayscale

import ImageSegmentation as isg
import ImageSeparation as isp
import ImagePreprocessing as ip



def loadimage(filename):
    """load the user file, .txt format"""    
    txtfile = np.loadtxt(filename, delimiter = '\t')
    
    return txtfile


def savefile(filename, file):
    output_file = np.savetxt(filename, file, fmt = '%.3f', delimiter = '\t')
    
    return output_file
    

def savecalculation(filename, file):
    output = np.empty((3, 2))
    output[:, 0] = ['order_to_disorder_ratio', 'percent_ordered', 'percent_disordered', 'percent_coverage']
    output[0, 1] = file[0]
    output[1, 1] = file[1]
    output[2, 1] = file[2]
    
    output_file = np.savetxt(filename, output, fmt = '%.3f', delimiter = '\t')

    return output_file



#runs one_k() and multiple_k() from command line
if __name__ == '__main__':
    print ('---AFM Image Segregation---')
    print ('Hello! Welcome to AFM Image Segregation!')
    print ('Please enter the filename WITHOUT .txt')
    
    user_filename = input('Filename: ')
    image = loadimage(user_filename + '.txt')


    #Perform image processing based on user's need    
    processing_need = input('How would you like to process the image?')
    

    if processing_need == 'Background Removal':
        #remove background and save corrected image
        bckgrnd_corr_image = ip.bckgrnd_corr(image)
        bkgnd_savefile = savefile(user_filename + 'bkgn_corr.txt', bckgrnd_corr_image)
        
        #convert image to grey-scale and save grey-scale image
        grayscale_image = ip.convert_to_grayscale(bckgrnd_corr_image)        
        grayscale_savefile = savefile(user_filename + 'bkgn_corr_grayscale.txt', grayscale_image)

    
    elif processing_need == 'Segregation':
        #remove background and save corrected image
        bckgrnd_corr_image = ip.bckgrnd_corr(image)
        bkgnd_savefile = savefile(user_filename + 'bkgn_corr.txt', bckgrnd_corr_image)
        
        #convert image to gray-scale and save gray-scale image
        grayscale_image = ip.convert_to_grayscale(bckgrnd_corr_image)        
        grayscale_savefile = savefile(user_filename + 'bkgn_corr_grayscale.txt', grayscale_image)
        
        #segment image
        segmented_image = isg.seg(grayscale_image)
        segmented_savefile = savefile(user_filename + 'segmented.txt', grayscale_image)
    
    
    elif processing_need == 'Separation':
        #remove background and save corrected image
        bckgrnd_corr_image = ip.bckgrnd_corr(image)
        bkgnd_savefile = savefile(user_filename + '_bkgn_corr.txt', bckgrnd_corr_image)
        
        #convert image to gray-scale and save gray-scale image
        grayscale_image = ip.convert_to_grayscale(bckgrnd_corr_image)        
        grayscale_savefile = savefile(user_filename + '_bkgn_corr_grayscale.txt', grayscale_image)
        
        #segment image
        segmented_image = isg.seg(grayscale_image)
        segmented_savefile = savefile(user_filename + '_segmented.txt', segmented_image)

        #separate images
        separated_image = isp.sep(segmented_image)
        filtered_savefile = savefile(user_filename + '_filtered.txt', separated_image[0])
        ordered_savefile = savefile(user_filename + '_ordered.txt', separated_image[1])
        disordered_savefile = savefile(user_filename + '_disordered.txt', separated_image[2])
        calculation_savefile = savecalculation(user_filename + '_disorder_calculation.txt', separated_image[3:])
                
        
    else:
        print ("Sorry! We can't help you...")
        
        exit
