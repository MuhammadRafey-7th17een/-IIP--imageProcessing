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



def sobelGx(window):
    kernel = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    value = 0
    for i in range(3):
        for j in range(3):
            value += (window[i, j]) * kernel[i, j]
    return np.clip(value,0,255)


def sobelGy(window):
    kernel = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ])
    value = 0
    for i in range(3):
        for j in range(3):
            value += (window[i, j]) * kernel[i, j]
    return np.clip(value,0,255)



def applySobelOperators(image):
    paddedImage = padImage(image, (3,3), "zero")
    img_h, img_w = image.shape

    output = np.zeros((img_h, img_w), dtype=np.uint8)

    for i in range(img_h):
        for j in range(img_w):
            window = paddedImage[i:i+3, j:j+3]

            gx = sobelGx(window)
            gy = sobelGy(window)

            magnitude = int(np.sqrt(gx*gx + gy*gy))
            output[i, j] = np.clip(magnitude, 0, 255)

    return output



