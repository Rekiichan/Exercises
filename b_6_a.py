import cv2 as cv

def showImg(src):
    img = cv.imread(src)
    cv.imshow(src,img)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    showImg('coins.png')