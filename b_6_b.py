from PIL import Image 
import cv2 as cv

img = Image.open("coins.png")
binaryImg = img.point(lambda x: 0 if x<128 else 255, '1')
binaryImg.save("binaryImg.png") #save it 
res = cv.imread('binaryImg.png')
ori = cv.imread('coins.png')
cv.imshow('original Img', ori)
cv.imshow('converted Img', res)
cv.waitKey()
cv.destroyAllWindows()