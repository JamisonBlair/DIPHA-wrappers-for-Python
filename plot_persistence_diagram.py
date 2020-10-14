#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:04:27 2020

@author: jamison
"""
import numpy as np
import matplotlib.pyplot as plt
from image_to_persistence_diagram import im2PD

def plot_PD(img, dual=False, superlevel=False, dimension=None):
    '''
    Parameters
    ----------
    img : str
        The directory of the image to be plotted as a persistence diagram
    
    dual : bool
        Option for running DIPHA. Sometimes faster. No visual difference.
        
    superlevel : bool
        If True, will act on the inverted version of the image.
    
    dimension : int (0 or 1)
        If either 0 or 1 is selected, will act only on 
        generators of that dimension.
    
    Returns
    -------
    None.
    
    Effect
    -------
    plots the persistence diagram in matplotlib.

    '''
    PD = im2PD(img, dual=dual, superlevel=superlevel)
    
    #infinity generator
    PD_inf = PD[PD[:,0] == -1,:][:,[1,2]]
    
    #0 dimensional generators
    PD_0 = PD[PD[:,0] == 0,:][:,[1,2]]
    
    #1 dimensional generators
    PD_1 = PD[PD[:,0] == 1,:][:,[1,2]]
    
    #close any open figures
    plt.close()
    
    #x and y figure limits
    xlim = (PD[:,1].min(),PD[:,2].max())
    ylim = (PD[:,1].min(),PD[:,2].max())
    
    #plot line y=x in figure
    plt.plot(xlim, ylim, c='#000000')
    
    #plot infinity generator
    plt.scatter(PD_inf[:,0],PD_inf[:,1], c='#000000', marker='d', s=15)
    
    #plot the 0 dimensional generators
    if dimension != 1:
        plt.scatter(PD_0[:,0],PD_0[:,1], edgecolor='black',linewidth=.33, label='Dimension 0', c='#779EF2', s=10)
    
    #plot the 1 dimensional generators
    if dimension != 0:
        plt.scatter(PD_1[:,0],PD_1[:,1],edgecolor='black',linewidth=.33, label='Dimension 1',c='#F27777', s=10)
    
    #plot the legend
    plt.legend()
    
    #show the plot
    plt.show()