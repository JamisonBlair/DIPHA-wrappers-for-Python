# DIPHA-wrappers-for-Python
Python scripts for working with the persistence homology on images, using the software package DIPHA. 
More information about DIPHA can be found here https://github.com/DIPHA/dipha.

The DIPHA software package comes with MATLAB functions to create the input files and visualize the data. The goal of this
package is to provide Python alternatives to these functions because I wanted to run DIPHA through Python.


## What's included:
1. **save_image_data.py**

  Contains the function *save_image_data* that takes in an image and
  writes its data into a binary file for DIPHA to process.

2. **load_persistance_diagram.py**

  Contains the function *load_persistence_diagram*
  which takes reads a processed DIPHA file and writes the information in a human
  readable numpy array.
  
3. **image_to_persistence_diagram.py**

  Contains the function *im2PD* which takes an image,
  runs it through DIPHA, and outputs the persistence diagram information
  as a numpy array.
  
4. **plot_persistence_diagram.py** 

  Contains the function *plot_PD* which takes an image and plots the (birth,death) points from
  its persistence diagram as a scatter plot in matplotlib.
  
5. A test image *diphaTEST.png* and its persistence diagram plotted in both DIPHA's 
MATLAB plotter and *plot_PD*, for comparison sanity checks after installing DIPHA.


## Using these files:
To use these files, it is assumed you have installed the DIPHA software on your machine. Instruction for this can be found
here https://github.com/DIPHA/dipha.

Once DIPHA is installed, simply place all these scripts in the same directory. You'll have to adjust lines 40 and 43 of 
*image_to_persistence_diagram.py* to include the path to *dipha*.

Have fun.
