import cv2 as cv
from PIL import Image as IM

def rotateImg(src, angle):
    img = IM.open(src)
    out = img.rotate(angle)
    out.save('1_2_rotated.tif')
    return out

if __name__ == "__main__":
    rotatedImg = rotateImg('1_2.tif', 45)
    img = cv.imread('1_2_rotated.tif')
    cv.imshow('Rotated Image', img)
    cv.waitKey()
    cv.destroyAllWindows()
    