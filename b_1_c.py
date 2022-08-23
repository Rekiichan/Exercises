import cv2 as cv
import numpy as np

def convertIntToDouble(src):
    img = cv.imread(src)
    res = img / 255
    cv.imshow('original', img)
    cv.imshow('converted Image', res)
    cv.waitKey()
    cv.destroyAllWindows()
    return res

if __name__ == "__main__":
    src = '1_4.bmp'
    res = convertIntToDouble(src)
