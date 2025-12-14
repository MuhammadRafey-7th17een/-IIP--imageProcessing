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


def SharpenFilter(window):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    value = 0
    for r in range(3):
        for c in range(3):
            value += window[r, c] * kernel[r, c]

    return np.clip(value, 0, 255)


def LaplacianEdgeDetection(window):
    kernel = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ])
    value = 0
    for r in range(3):
        for c in range(3):
            value += window[r, c] * kernel[r, c]

    return np.clip(value, 0, 255)


def LaplacianEdgeDetectionDiagonal(window):
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])
    value = 0
    for r in range(3):
        for c in range(3):
            value += window[r, c] * kernel[r, c]

    return np.clip(value, 0, 255)


def applyLaplacianFilter(image, filterType="sharpen"):
    paddedImage = padImage(image, (3,3), "zero")
    output = np.zeros_like(image)
    img_h, img_w = image.shape

    for i in range(img_h):
        for j in range(img_w):
            window = paddedImage[i:i+3, j:j+3]

            if filterType.lower() == "sharpen":
                value = SharpenFilter(window)
            elif filterType.lower() == "edgedetection":
                value = LaplacianEdgeDetection(window)
            elif filterType.lower() == "diagonaledgedetection":
                value = LaplacianEdgeDetectionDiagonal(window)
            else:
                raise ValueError("Invalid filter type")

            output[i, j] = value

    return output

