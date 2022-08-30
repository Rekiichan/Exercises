import numpy as np
import cv2 as cv

initial_image = np.array([[255,87], 
                          [150,30]])

print("\nIN(8 bits):")
print(initial_image)
print('\n')
# r,c = initial_image.shape

scale = pow(2,8) / pow(2,5)
out5 = initial_image / scale
out5 = np.floor(out5)
out5 = out5*scale + scale/2
print("OUT(5 bits):")
print(out5)
print('\n')

scale = pow(2,8) / pow(2,3)
out3 = initial_image / scale
out3 = np.floor(out3)
out3 = out3*scale + scale/2  
print("OUT(3 bits):")
print(out3)
print('\n')
