from PIL import Image 
import cv2 as cv

img = Image.open("coins.png")
binaryImg = img.point(lambda x: 0 if x<128 else 255, '1')
asaa = img.point()
cv.imread(binaryImg)
cv.imshow('asasa', binaryImg)
# binaryImg.save("test_bw.png") #save it 