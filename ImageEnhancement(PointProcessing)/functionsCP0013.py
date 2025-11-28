import numpy as np

def identity(matrix):
    
    return matrix

def negativeImage(matrix):
    
    return 255-matrix

def thresholding(matrix,threshold):
    image = matrix.copy()
    image[image>threshold] = 255
    image[image<=threshold] = 0
    return image

def scaleImageBrightness(matrix,scaleFactor):
   
    
    return scaleFactor*matrix

def logrithmeticTransformation(matrix,constant):
    image = matrix.copy()
    image = image.astype(float)
    image = constant*np.log(1+image)
    image = (image/np.max(image))*255
    return image

def antiLogrithmeticTransformation(matrix,constant):
    image = matrix.copy()
    image = image.astype(float)
    image = image / 255.0
    image = constant*(np.exp(image)-1)
    image = (image/np.max(image))*255
    return image

def gammaTransformation(matrix,constant,gamma):
    image = matrix.copy()
    image = image.astype(float)
    image = image / 255
    image = constant*(np.power(image,gamma))
    image = (image / np.max(image)) * 255
    return image

def greyLevelSlicingMaintained(matrix,low,high):
    image = matrix.copy()
    booleanMask = (image>=low)&(image<=high)
    image[booleanMask] = 255
    return image

def greyLevelSlicing(matrix,low,high):
    image = matrix.copy()
    booleanMask = (image>=low)&(image<=high)
    image[booleanMask] = 255
    image[~booleanMask] = 0
    return image




