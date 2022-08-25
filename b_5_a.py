import numpy as np
import cv2 as cv

initial_image = np.array([[255,87], 
                  [150,30]])

print("IN(8 bits):")
print(initial_image)
print('\n')

scale = pow(2,11) / pow(2,8)
output11 = initial_image * scale
output11 = np.round_(output11)
print("OUT(11 bits):")
print(output11)
print('\n')

scale = 32 / 255
output5 = initial_image * scale
output5 = np.round_(output5)
print("OUT(5 bits):")
print(output5)
print('\n')

scale = 8 / 255
output3 = initial_image * scale
output3 = np.round_(output3)
print("OUT(3 bits):")
print(output3)
