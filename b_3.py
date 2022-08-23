import numpy as np
import cv2 as cv

def process(src):
    img = cv.imread(src) 
    crop_img_1 = img[0:63, 0:63]
    crop_img_2 = img[64:127, 0:63]
    crop_img_3 = img[0:63, 64:127]
    crop_img_4 = img[64:127, 64:127]
    
    cv.imshow("cropped", crop_img_1)
    cv.imshow("original", img)
    cv.waitKey()
    cv.destroyAllWindows()

    cv.imshow("cropped", crop_img_2)
    cv.imshow("original", img)
    cv.waitKey()
    cv.destroyAllWindows()
    
    cv.imshow("cropped", crop_img_3)
    cv.imshow("original", img)
    cv.waitKey()
    cv.destroyAllWindows()
    
    cv.imshow("cropped", crop_img_4)
    cv.imshow("original", img)
    cv.waitKey()
    cv.destroyAllWindows()



if __name__ == "__main__":
    process('1_2.tif')