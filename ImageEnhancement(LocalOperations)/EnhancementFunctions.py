import numpy as np

# --------------------- 1. Image Padding ---------------------
def padImage(image, filter_shape, padding_type="zero"):
    image_height, image_width = image.shape
    f_h, f_w = filter_shape
    p_h, p_w = f_h // 2, f_w // 2

    new_h, new_w = image_height + 2*p_h, image_width + 2*p_w
    paddedImage = np.zeros((new_h, new_w), dtype=image.dtype)

    # center image
    paddedImage[p_h:p_h+image_height, p_w:p_w+image_width] = image

    if padding_type.lower() == "zero":
        return paddedImage

    elif padding_type.lower() == "replicate":
        # top & bottom
        paddedImage[:p_h, p_w:p_w+image_width] = image[0:1, :]
        paddedImage[p_h+image_height:, p_w:p_w+image_width] = image[-1:, :]
        # left & right
        paddedImage[:, :p_w] = paddedImage[:, p_w:p_w+1]
        paddedImage[:, p_w+image_width:] = paddedImage[:, p_w+image_width-1:p_w+image_width]
        return paddedImage

    else:
        print("Invalid padding type")
        quit()

# --------------------- 2. Get Window ---------------------
def Get_Window(pad_img, filter_shape, row, col):
    image_height,image_width = pad_img.shape
    f_h,f_w = filter_shape

    p_h = f_h//2
    p_w = f_w//2

    windowRowStart = row-p_h
    windowRowEnd = row+p_h+1
    windowColsStart = col-p_w
    windowColsEnd = col+p_w+1

    if windowRowStart < 0 or windowColsStart < 0 or windowRowEnd > image_height or windowColsEnd > image_width:
        print("Window function error\n")
        quit()
    
    return pad_img[windowRowStart:windowRowEnd,windowColsStart:windowColsEnd].copy()

# --------------------- 3. Statistical Filters ---------------------
def minFilter(window, filter_shape):
    f_h, f_w = filter_shape
    minimum = window[0,0]
    for i in range(f_h):
        for j in range(f_w):
            if window[i,j] < minimum:
                minimum = window[i,j]
    return minimum

def maxFilter(window, filter_shape):
    f_h, f_w = filter_shape
    maximum = window[0,0]
    for i in range(f_h):
        for j in range(f_w):
            if window[i,j] > maximum:
                maximum = window[i,j]
    return maximum

def meanFilter(window, filter_shape):
    f_h, f_w = filter_shape
    total = 0
    for i in range(f_h):
        for j in range(f_w):
            total += window[i,j]
    return total / (f_h*f_w)

def medianFilter(window, filter_shape):
    # flatten the 2D window into a 1D list
    arr = window.flatten()  # built-in allowed
    arr = list(arr)         # ensure it’s a Python list

    # sort manually or use sorted()
    arr.sort()              # now arr is sorted

    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        # if even, take average of middle two
        return (arr[mid-1] + arr[mid]) / 2
    else:
        # if odd, take middle element
        return arr[mid]

def weightedAverageFilter(window, filter_shape, sigma=1.0):
    """
    window       : 2D numpy array (same shape as filter)
    filter_shape : tuple (rows, cols)
    sigma        : standard deviation of Gaussian
    Returns weighted average (Gaussian) value for this window
    """
    f_h, f_w = filter_shape
    kernel = np.zeros((f_h, f_w), dtype=float)
    c_h, c_w = f_h // 2, f_w // 2

    # Generate Gaussian kernel
    for i in range(f_h):
        for j in range(f_w):
            x = j - c_w # gives cordinate relative to center
            y = i - c_h
            kernel[i,j] = np.exp(-(x**2 + y**2)/(2*sigma**2))
    
    # Normalize kernel so sum = 1
    kernel /= np.sum(kernel)

    # Compute weighted sum
    total = 0
    for i in range(f_h):
        for j in range(f_w):
            total += window[i,j] * kernel[i,j]

    return total



# --------------------- 5. Apply Statistical Filter to whole image ---------------------
def applyStatisticalFilter(image, filter_shape, padding_type, method):
    img_h, img_w = image.shape
    padded = padImage(image, filter_shape, padding_type)
    output = np.zeros_like(image)
    f_h, f_w = filter_shape
    p_h, p_w = f_h//2, f_w//2

    for i in range(img_h):
        for j in range(img_w):
            # get window centered on padded image
            window = Get_Window(padded, filter_shape, i+p_h, j+p_w)

            if method.lower() == "min":
                value = minFilter(window, filter_shape)
            elif method.lower() == "max":
                value = maxFilter(window, filter_shape)
            elif method.lower() == "median":
                value = medianFilter(window, filter_shape)
            elif method.lower() == "average":
                value = meanFilter(window, filter_shape)
            elif method.lower() == "weighted":
                value = weightedAverageFilter(window,filter_shape,1)
            else:
                value = 0

            output[i,j] = value

    return output


# def Get_Window(pad_img,filter_shape,row,col):
#     image_height,image_width = pad_img.shape
#     f_h,f_w = filter_shape

#     p_h = f_h//2
#     p_w = f_w//2

#     windowRowStart = row-p_h
#     windowRowEnd = row+p_h+1
#     windowColsStart = col-p_w
#     windowColsEnd = col+p_w+1

#     if windowRowStart < 0 or windowColsStart < 0 or windowRowEnd > image_height or windowColsEnd > image_width:
#         print("Window function error\n")
#         quit()
    

#     return pad_img[windowRowStart:windowRowEnd,windowColsStart:windowColsEnd].copy()








# # Function to print nicely
# def print_matrix(mat):
#     for row in mat:
#         print(' '.join(f"{int(x):2}" for x in row))
#     print("\n")

# # Test images
# image_3x3 = np.array([[1,2,3],
#                       [4,5,6],
#                       [7,8,9]])

# image_7x7 = np.arange(1, 50).reshape(7,7)

# filter_shape = (3,3)  # example

# # Padding types
# padding_types = ["zero", "replicate", "mirror", "wrap"]

# print("===== 3x3 IMAGE =====\n")
# for p_type in padding_types:
#     print(f"Padding type: {p_type.upper()}")
#     padded = padImage(image_3x3, filter_shape, p_type)
#     print_matrix(padded)

# print("===== 7x7 IMAGE =====\n")
# for p_type in padding_types:
#     print(f"Padding type: {p_type.upper()}")
#     padded = padImage(image_7x7, filter_shape, p_type)
#     print_matrix(padded)





    

