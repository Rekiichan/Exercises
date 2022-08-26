from PIL import Image 
import cv2 as cv
import numpy as np

def process(src):

    Init_Image = cv.imread(src)
    rows,cols,h = Init_Image.shape
    converted_img = np.zeros((rows,cols,h))

    for row in range(0,rows):
        for col in range(0,cols):
            if (Init_Image[row][col][0] >= 128):
                converted_img[row][col] = 255
            else:
                converted_img[row][col] = 0
                
    return Init_Image, converted_img

if __name__ == "__main__":
    init_image, converted_img = process("coins.png")
    cv.imshow('original Img', init_image)
    cv.imshow('converted Img', converted_img)
    cv.waitKey()
    cv.destroyAllWindows()

