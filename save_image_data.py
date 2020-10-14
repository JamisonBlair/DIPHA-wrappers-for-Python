#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:00:31 2020

@author: jamison
"""
import struct
import math
import numpy as np
import matplotlib.image as mpimg

def save_image_data(img, superlevel=False):
    '''
    Converts image into data for DIPHA to read.
    Writes a binary file 'diphin' in current directory
    If the image is not grayscale, it converts to a nonunique grayscale version.

    Parameters
    ----------
    img : an image file

    Returns
    -------
    None.

    '''
    
    c_image = mpimg.imread(img) #reads image in
    
    #if c_image is a 3D array, this will convert it a 1D array using 
    #the rgb_wieghts.
    rgb_weights = [0.2989, 0.5870, 0.1140]
    if len(c_image.shape) == 3:
        g_image = np.dot(c_image[...,:3], rgb_weights)
    else:
        g_image = c_image
        
    #if superlevel is True, the following essentially inverts the image.
    if superlevel:
        g_image = math.ceil(g_image.max())-g_image
        
    #useful values    
    im_data = g_image.shape
    data_size = im_data[0]*im_data[1]
    data_len = len(im_data)
    
    #Creates the file diphin and writes various ID 
    #information (as litte-endian int64 "<q") about
    #the image for DIPHA. First line is the DIPHA magic number.
    #Next, is the file typ identifier.
    fid = open('diphin', 'wb')
    fid.write(struct.pack('<q',8067171840))
    fid.write(struct.pack('<q',1))
    fid.write(struct.pack('<q',data_size))
    fid.write(struct.pack('<q',data_len))
    fid.write(struct.pack('<q',im_data[0]))
    fid.write(struct.pack('<q',im_data[1]))
    
    #Writes the actual data in x-fastest order (MATLAB?).
    for i in np.nditer(g_image.T, order='C'):
        fid.write(struct.pack('d',i))
    
    #close file.
    fid.close()