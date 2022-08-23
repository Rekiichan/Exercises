import cv2 as cv

def rgb2gray(src):
    img = cv.imread(src, 0)
    grayImg = cv.cvtColor(img, cv.COLOR_BAYER_BG2GRAY)
    return grayImg    
    
if __name__ == "__main__":
    imgGray = rgb2gray('1_2.tif')
    imgRgb = cv.imread('1_2.tif')
    cv.imshow('image rgb', imgRgb)
    cv.imshow('image gray', imgGray)
    cv.waitKey()
    cv.destroyAllWindows()
    