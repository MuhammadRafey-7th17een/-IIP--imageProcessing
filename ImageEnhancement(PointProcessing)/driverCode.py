import functionsCP0013 as func
import matplotlib.pyplot as plt
import skimage.io as skio


print("Following methods available")
print("1.Identity\n2.Negative\n3.Thresholding\n4.ScaledImage\n5.Logirithm\n6.Anti-Log\n7.Power Transform\n8.Piece Wise Contrast-Strecthing\n9.GrayLevelSlicing\n10.BitPlaneSlicing\n11.InterpolatedImage")
print("Press 0 to exit\n")


while(True):
    try:
        method = int(input("Enter method: "))
    except:
        print("Invalid data type of method")
        method = -1
    if(method == 1):
        pth = input("Enter image path: ")
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        identityimg = func.identity(img)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(identityimg,cmap='gray')
        ax[1].set_title("Identity Image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 2):
        pth = input("Enter image path: ")
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        negativeImage = func.negativeImage(img)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(negativeImage,cmap='gray')
        ax[1].set_title("NegativeImage")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 3):
        pth = input("Enter image path: ")
        try:
            thresholdvalue = int(input("Enter threshold value: "))
        except:
            print("Invalid data type")
            quit()
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        thresholdImg = func.thresholding(img,thresholdvalue)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(thresholdImg,cmap='gray')
        ax[1].set_title("Threshold image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 4):
        pth = input("Enter image path: ")
        try:    
            scaleFactor = int(input("Enter scale factor: "))
        except:
            print("Invalid data type")
            quit()
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        scaledImg = func.scaleImageBrightness(img,scaleFactor)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(scaledImg,cmap='gray')
        ax[1].set_title("Scaled Image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 5):
        pth = input("Enter image path: ")
        try:
            constant = int(input("Enter constant value: "))
        except:
            print("Invalid data type")
            quit()
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        logImg = func.logrithmeticTransformation(img,constant)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(logImg,cmap='gray')
        ax[1].set_title("Log Image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 6):
        pth = input("Enter image path: ")
        try:
            constant = int(input("Enter constant value: "))
        except:
            print("Invalid data type")
            quit()
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        antiLogImg = func.antiLogrithmeticTransformation(img,constant)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(antiLogImg,cmap='gray')
        ax[1].set_title("antiLog Image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 7):
        pth = input("Enter image path: ")
        try:
            constant = int(input("Enter constant value: "))
            gamma = float(input("Enter gamma value: "))
        except:
             print("Invalid data types")
             quit()
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        gammaImg = func.gammaTransformation(img,constant,gamma)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(gammaImg,cmap='gray')
        ax[1].set_title("Power Law Image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()      
    elif(method == 8):
        print("Method for piecewise\nbitplane\ninterpolated wasnt implemented rest are functional")
    elif(method == 9):
        pth = input("Enter image path: ")
        try:
            low = int(input("Enter value for low: "))
            high = int(input("Enter value for high: "))
        except:
            print("Invalid data types")
            quit()
        try:
            img = skio.imread(pth, as_gray = True)
        except:
            print("imread error, invalid path probaility\n")
            quit()
        slicedImg = func.greyLevelSlicing(img,low,high)
        fig, ax = plt.subplots(1,2)
        ax[0].imshow(img,cmap='gray')
        ax[0].set_title("Original image")
        ax[1].imshow(slicedImg,cmap='gray')
        ax[1].set_title("Grey level slicied Image")
        plt.suptitle("Muhammad Rafey - L1F23BSCS0013")
        plt.show()
        plt.close()
    elif(method == 10):
        print("Method for piecewise\nbitplane\ninterpolated wasnt implemented rest are functional")
    elif(method == 11):
        print("Method for piecewise\nbitplane\ninterpolated wasnt implemented rest are functional")
    elif(method == 0):
        break
    else:
        print("Invalid commmand\n")

    





    

    




