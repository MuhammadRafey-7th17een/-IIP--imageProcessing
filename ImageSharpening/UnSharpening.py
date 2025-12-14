import numpy as np

def padImage(image, filter_shape, padding_type="zero"):
    image_height, image_width = image.shape
    f_h, f_w = filter_shape
    p_h, p_w = f_h // 2, f_w // 2

    new_h, new_w = image_height + 2*p_h, image_width + 2*p_w
    paddedImage = np.zeros((new_h, new_w), dtype=image.dtype)

    # center image
    paddedImage[p_h:p_h+image_height, p_w:p_w+image_width] = image

    padding_type = padding_type.lower()

    # ---------------- ZERO ----------------
    if padding_type == "zero":
        return paddedImage

    # ---------------- WHITE ----------------
    elif padding_type == "white":
        paddedImage[:] = 255
        paddedImage[p_h:p_h+image_height, p_w:p_w+image_width] = image
        return paddedImage

    # ---------------- REPLICATE ----------------
    elif padding_type == "replicate":
        # top & bottom
        paddedImage[:p_h, p_w:p_w+image_width] = image[0:1, :]
        paddedImage[p_h+image_height:, p_w:p_w+image_width] = image[-1:, :]

        # left & right
        paddedImage[:, :p_w] = paddedImage[:, p_w:p_w+1]
        paddedImage[:, p_w+image_width:] = paddedImage[:, p_w+image_width-1:p_w+image_width]
        return paddedImage

    # ---------------- MIRROR / REFLECT ----------------
    elif padding_type == "mirror":
        for i in range(p_h):
            paddedImage[p_h-1-i, p_w:p_w+image_width] = image[i, :]
            paddedImage[p_h+image_height+i, p_w:p_w+image_width] = image[-1-i, :]

        for j in range(p_w):
            paddedImage[:, p_w-1-j] = paddedImage[:, p_w+j]
            paddedImage[:, p_w+image_width+j] = paddedImage[:, p_w+image_width-1-j]

        return paddedImage

    # ---------------- WRAP AROUND / CIRCULAR ----------------
    elif padding_type == "wrap":
        for i in range(p_h):
            paddedImage[i, p_w:p_w+image_width] = image[-p_h+i, :]
            paddedImage[p_h+image_height+i, p_w:p_w+image_width] = image[i, :]

        for j in range(p_w):
            paddedImage[:, j] = paddedImage[:, p_w+image_width-p_w+j]
            paddedImage[:, p_w+image_width+j] = paddedImage[:, p_w+j]

        return paddedImage

    else:
        raise ValueError("Invalid padding type")

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

def meanFilter(window, filter_shape):
    f_h, f_w = filter_shape
    total = 0
    window_i = window.astype(np.int32)
    for i in range(f_h):
        for j in range(f_w):
            total += window_i[i,j]
    return total // (f_h*f_w)


def smoothing(image,filterShape):
    img_h,img_w = image.shape
    f_h,f_w = filterShape
    paddedImage = padImage(image,filterShape,"zero")
    p_h = f_h//2
    p_w = f_w//2
    output = np.zeros_like(image)
    for i in range(img_h):
        for j in range(img_w):
            window = Get_Window(paddedImage,filterShape,i+p_h,j+p_w)
            value = meanFilter(window,filterShape)
            output[i,j] = value
    
    return output


def Unsharp(image, filterShape, weight=1):
    blur = smoothing(image, filterShape)

    # convert to int to avoid overflow
    image_i = image.astype(np.int16)
    blur_i  = blur.astype(np.int16)

    mask = image_i - blur_i
    unsharpImage = image_i + weight * mask

    # clip to valid grayscale range
    unsharpImage = np.clip(unsharpImage, 0, 255)

    return unsharpImage.astype(np.uint8)
