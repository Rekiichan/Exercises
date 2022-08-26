import cv2 as cv

if __name__ == "__main__":
    img = cv.imread('1_4.bmp')
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

