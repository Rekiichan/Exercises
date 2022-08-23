import cv2 as cv
import numpy as np

def getType(src):
    res = cv.imread(src).dtype
    return res

def getMinMaxOfImg(src):
    img = cv.imread(src)
    smallest = np.amin(img)
    largest = np.amax(img)
    return smallest, largest

if __name__ == "__main__":
    type = getType('1_4.bmp')
    print('Type:', type)
    minVal, maxVal = getMinMaxOfImg('1_4.bmp')
    print('Min data value:', minVal)
    print('Max data value:', maxVal)