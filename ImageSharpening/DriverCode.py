import matplotlib.pyplot as plt
import UnSharpening as unsharp
import SharpeningFunctions as sharpFunc
import Sobel
import skimage.io as skio




def SharpeningDriverCode():
    try:
        pth = input("Enter image path: ")
        img = skio.imread(pth,as_gray=True)
    except:
        print("Error in path or image Opening")
    
    method = input("Enter Method: ")
    if method.lower() == "sharpen":
        output = sharpFunc.applyLaplacianFilter(img,"sharpen")
    elif method.lower() == "edgedetection":
        output = sharpFunc.applyLaplacianFilter(img,"edgedetection")
    elif method.lower() == "diagonaledgedetection":
        output = sharpFunc.applyLaplacianFilter(img,"diagonaledgedetection")
    else:
        print("InvalidOption\n")
        quit()
    fig,ax = plt.subplots(1,2,figsize = (10,10))
    ax[0].imshow(img,cmap='gray')
    ax[0].set_title("Original")
    ax[1].imshow(output,cmap='gray')
    ax[1].set_title(method)
    plt.show()
    plt.close()
    

def unsharpDiver():
    try:
        pth = input("Enter image path: ")
        img = skio.imread(pth,as_gray=True)
    except:
        print("Error in reading or opening\n")
        quit()
    try:
        weight = int(input("Enter weight: "))
    except:
        print("Invalid weight given\n")
        quit()
    unSharpedImage = unsharp.Unsharp(img,(3,3),weight)
    fig,ax = plt.subplots(1,2,figsize = (10,10))
    ax[0].imshow(img,cmap='gray')
    ax[0].set_title("Original")
    ax[1].imshow(unSharpedImage,cmap='gray')
    ax[1].set_title("UnSharped")
    plt.show()
    plt.close()



def sobeldriver():
    try:
        pth = input("Enter path of image: ")
        img = skio.imread(pth,as_gray=True)
    except:
        print("Error in image read or open\n")
        quit()
    
    FilteredImage = Sobel.applySobelOperators(img)
    fig,ax = plt.subplots(1,2,figsize = (10,10))
    ax[0].imshow(img,cmap='gray')
    ax[0].set_title("Original")
    ax[1].imshow(FilteredImage,cmap='gray')
    ax[1].set_title("Sobel")
    plt.show()
    plt.close()


def main():
    print("Press 1 for Sharpening\n2 For Unsharpening\n3 for Sobel edge")
    method = int(input("Enter: "))
    if method > 3 or method < 0:
        print("Invalid method\n")
        quit()
    if method == 1:
        SharpeningDriverCode()
    elif method == 2:
        unsharpDiver()
    elif method == 3:
        sobeldriver()









if __name__ == "__main__":
    main()