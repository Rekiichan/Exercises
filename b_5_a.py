import numpy as np

input = np.array([[255,87], 
              [150,30]])
print("IN(8 bits):")
print(input)
print('\n')

output11 = input * 2047 / 255
output11 = np.round_(output11)
print("OUT(11 bits):")
print(output11)
print('\n')

output5 = input * 32 / 255
output5 = np.round_(output5)
print("OUT(5 bits):")
print(output5)
print('\n')

output3 = input * 8 / 255
output3 = np.round_(output3)
print("OUT(3 bits):")
print(output3)
