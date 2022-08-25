import cv2 as cv

def convertIntToDouble(src):
    img = cv.imread(src)
    res = img / 255
    cv.imshow('original', img)
    cv.imshow('converted Image', res)
    cv.waitKey()
    cv.destroyAllWindows()
    return res

if __name__ == "__main__":
    res = convertIntToDouble('1_4.bmp')
