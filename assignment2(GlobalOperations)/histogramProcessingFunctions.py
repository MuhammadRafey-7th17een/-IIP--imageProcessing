import numpy as np


def histogramContrastStrecthing(matrix):
    image = matrix.copy().astype(float)
    fmin = np.min(image)
    fmax = np.max(image)
    if(fmin == fmax):
        print("minPixelValue = maxPixelValue")
    
        return image.astype(np.uint8)
    
    image = ((image-fmin)/(fmax-fmin))*255
    return image.astype(np.uint8)

def histogramEqualisation(matrix):
    image = matrix.copy()

    histogram,bin = np.histogram(image,bins=256,range=(0,255))
    totalPixels = np.sum(histogram)
    pmf = list()
    for i in histogram:
        pmf.append(i/totalPixels)
    
    cdf = list()
    cumulativeSum = 0
    for i in range(256):
        cumulativeSum += pmf[i]
        cdf.append(cumulativeSum*255)
    cdf = np.array(cdf) 
    image = cdf[image]
    return image.astype(np.uint8)
    
    

#debugging

# def main():
#     img = skio.imread("Assignment 1 dataset/Mamogram.tif")
#     histogramEqualisation(img)


# if __name__ == "__main__":
#     main()
    





