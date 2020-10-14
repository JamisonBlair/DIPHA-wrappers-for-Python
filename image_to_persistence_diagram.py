#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:30:48 2020

@author: jamison
"""
import os
from save_image_data import save_image_data
from load_persistence_diagram import load_persistence_diagram

def im2PD(img, dual=False, superlevel=False):
    '''
    Parameters
    ----------
    img : str
        directory of an image to be processed by DIPHA.
    dual : bool
        option for DIPHA that sometimes speeds up computation.
    superlevel: bool.
        if True, applies DIPHA to the inverted image.
        
        
    Returns : per_diagram
    -------
    The DIPHA persistence diagram as a (n,3) numpy array based
    on a grayscaled version of the image.
    The first row is  the inf marker. The other n-1 rows
    are the (dim, birth, death) info for each generator of the 
    persistence diagram.
    '''
    
    #save image data in binary file diphin for DIPHA to process.
    save_image_data(img, superlevel=superlevel)
    
    #run DIPHA (or dual of DIPHA) on diphin file.
    #outputs file diphout in current directory.
    if dual:
	#replace dipha with [path to directory holding dipha]/dipha
        os.system('dipha --dual "diphin" "diphout"')
    else:
	#replace dipha with [path to directory holding dipha]/dipha    
        os.system('dipha "diphin" "diphout"')
    
    #read DIPHA output diphout into human readable numpy array.
    per_diag = load_persistence_diagram("diphout")
    
    return per_diag