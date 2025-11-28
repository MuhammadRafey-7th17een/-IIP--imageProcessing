import numpy as np
import skimage.io as skio
import matplotlib.pyplot as plt

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
    cummulativeSum = 0
    for i in range(256):
        cummulativeSum += pmf[i]
        cdf.append(cummulativeSum*255)
    cdf = np.array(cdf) 
    image = cdf[image]
    return image.astype(np.uint8)
   

def main():

    print("1.HistogramStrecthing\n2.HistogramEqualisation")
    method = int(input("Enter method: "))

    if(method == 1):
        pth = input("Enter image path: ")
        try:
            img = skio.imread(pth,as_gray =True)
        except:
            print("Image read error")
            quit()
        strecthedImage = histogramContrastStrecthing(img)
        fig,ax = plt.subplots(2,2,figsize=(10,10))
        ax[0][0].imshow(img,cmap='gray')
        ax[0][0].set_title("Original image")
        ax[0][1].hist(img.ravel(),bins = 256, range=(0,255),color = 'gray')
        ax[0][1].set_title("Orginal histogram")
        ax[0][1].set_xlabel("Pixel intensity")
        ax[0][1].set_ylabel("Frequency")
        ax[1][0].imshow(strecthedImage,cmap='gray')
        ax[1][0].set_title("Strechted image")
        ax[1][1].hist(strecthedImage.ravel(),bins = 256, range=(0,255),color = 'gray')
        ax[1][1].set_title("New histogram")
        ax[1][1].set_xlabel("Pixel intensity")
        ax[1][1].set_ylabel("Frequency")
        plt.show()
        plt.close()
    elif(method == 2):
        pth = input("Enter image path: ")
        try:
            img = skio.imread(pth,as_gray =True)
        except:
            print("Image read error")
            quit()
        equalisedImage = histogramEqualisation(img)
        fig,ax = plt.subplots(2,2,figsize=(10,10))
        ax[0][0].imshow(img,cmap='gray')
        ax[0][0].set_title("Original image")
        ax[0][1].hist(img.ravel(),bins = 256, range=(0,255),color = 'gray')
        ax[0][1].set_title("Orginal histogram")
        ax[0][1].set_xlabel("Pixel intensity")
        ax[0][1].set_ylabel("Frequency")
        ax[1][0].imshow(equalisedImage,cmap='gray')
        ax[1][0].set_title("Equalised image")
        ax[1][1].hist(equalisedImage.ravel(),bins = 256, range=(0,255),color = 'gray')
        ax[1][1].set_title("New histogram")
        ax[1][1].set_xlabel("Pixel intensity")
        ax[1][1].set_ylabel("Frequency")
        plt.show()
        plt.close()
    else:
        print("Invalid command chosen run again")
        



#main call
if __name__ == "__main__":
    main()


         