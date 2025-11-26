import numpy as np
import matplotlib.pyplot as plt
import skimage.io as skio
import EnhancementFunctions as func


def driverCode(choice,paddingType):
    
    pth = input("Image path: ")
    x = int(input("Enter number of rows of filter shape: "))
    y = int(input("Enter number of cols of filter shape: "))
    
    if x < 0 or y <0:
        print("Invalid filter shape")
        quit()
    try:
        image = skio.imread(pth,as_gray=True)
    except:
        print("Error opening image")
        quit()
    if choice == 1:
        try:
            output = func.applyStatisticalFilter(image,(x,y),paddingType,"min")
        except:
            print("Error in apllying min filter")
        fig,ax = plt.subplots(1,2,figsize = (10,10))
        ax[0].imshow(image,cmap='gray')
        ax[0].set_title("Orginal")
        ax[1].imshow(output,cmap='gray')
        ax[1].set_title("Min")
        plt.show()
        plt.close()
    elif choice == 2:
        try:
            output = func.applyStatisticalFilter(image,(x,y),paddingType,"max")
        except:
            print("Error in apllying min filter")
        fig,ax = plt.subplots(1,2,figsize = (10,10))
        ax[0].imshow(image,cmap='gray')
        ax[0].set_title("Orginal")
        ax[1].imshow(output,cmap='gray')
        ax[1].set_title("Max")
        plt.show()
        plt.close()
    elif choice == 3:
        try:
            output = func.applyStatisticalFilter(image,(x,y),paddingType,"median")
        except:
            print("Error in apllying min filter")
        fig,ax = plt.subplots(1,2,figsize = (10,10))
        ax[0].imshow(image,cmap='gray')
        ax[0].set_title("Orginal")
        ax[1].imshow(output,cmap='gray')
        ax[1].set_title("Median")
        plt.show()
        plt.close()
    elif choice == 4:
        try:
            output = func.applyStatisticalFilter(image,(x,y),paddingType,"average")
        except:
            print("Error in apllying min filter")
        fig,ax = plt.subplots(1,2,figsize = (10,10))
        ax[0].imshow(image,cmap='gray')
        ax[0].set_title("Orginal")
        ax[1].imshow(output,cmap='gray')
        ax[1].set_title("Average")
        plt.show()
        plt.close()
    elif choice == 5:
        try:
            output = func.applyStatisticalFilter(image,(x,y),paddingType,"weighted")
        except:
            print("Error in apllying min filter")
        fig,ax = plt.subplots(1,2,figsize = (10,10))
        ax[0].imshow(image,cmap='gray')
        ax[0].set_title("Orginal")
        ax[1].imshow(output,cmap='gray')
        ax[1].set_title("Weighted")
        plt.show()
        plt.close()
    

        


    
    



def main():
    
    print("Spatial Filters Avaliable are:\n1.Min\n2.Max.\n3.Median\n4.Average\n5.Weighted\n")
    method = int(input("Enter method: ")) 
    if(method in range(1,6)):
        paddingType = input("Enter padding type: ")
        driverCode(method,paddingType)
    else:
        print("Invalid method can't apply")    





if __name__ == "__main__":
    main()