import numpy as np
import cv2 as cv

def process(src):
    img = cv.imread(src)
    res = cv.imread(src) 
    rows = len(img)
    cols = len(img[0])
    for hang in range(0,4):
        for cot in range(0,4):
            i = 3 - hang
            j = 3 - cot
            for k in range(0,32):
                for l in range(0,32):
                    res[i*32 + k][j*32 + l] = img[hang*32 + k][cot*32 + l]
            

    cv.imshow('original img', img)
    cv.imshow('converted img', res)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    process('1_2.tif')