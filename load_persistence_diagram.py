#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:00:33 2020

@author: jamison
"""

import struct
import numpy as np


def load_persistence_diagram(diphout):
    '''
    Loads the data DIPHA outputs into a human readable persistence diagram.

    Parameters
    ----------
    diphout : An output from dipha.

    Returns
    -------
    returns a numpy array with each row corresponding to a generator of the
    persistence diagram. First column is the dimension, second column is the 
    birth value, third column is the death value.

    '''
    #opens the file the output from DIPHA, diphout.
    file = open(diphout, "rb")
    
    #checks if diphout is actually a DIPHA file by checking the magic number.
    dipha_identifier = int.from_bytes(file.read(8), byteorder='little', signed=True)
    assert dipha_identifier == 8067171840, 'input is not a DIPHA file'
    
    #checks if diphout is in fact a persistence diagram.
    diagram_identifier = int.from_bytes(file.read(8), byteorder='little', signed=True)
    assert diagram_identifier == 2, 'input is not a persistence diagram'
    
    #number of generators
    num_pairs = int.from_bytes(file.read(8), byteorder='little', signed=True)
    
    #containers for the dimensions, births, and deaths.
    dims = []
    births = []
    deaths = []
    
    #Loops over num_pairs. Each iteration corresponds to 24 bits.
    #8 for the dimension, 8 for the birth value, 8 for the death value.
    #Appends the respective containers and decreases the value of num_pairs.
    while num_pairs > 0:
        dim = int.from_bytes(file.read(8), byteorder='little', signed=True)
        birth = struct.unpack('d', file.read(8))[0]
        death = struct.unpack('d', file.read(8))[0]
        
        dims.append(dim)
        births.append(birth)
        deaths.append(death)
        num_pairs = num_pairs - 1
    #once the file has been read, we close it.
    file.close()
    
    #returns a (num_pairs, 3) numpy array.
    #columns are dim, bith, death.
    #rows correspond to generators of the persistence diagram.
    return np.array([dims, births, deaths]).T
    