from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

mat = np.loadtxt('1_3.asc') # skiprows=6
res = np.copy(mat)
rows = len(mat)     #384 / 4 = 96
cols = len(mat[0])  #256 / 4 = 64
out = cv.resize(src=mat, dsize=(64, 96))
    
fig = plt.figure(figsize=(10, 7)) #create figure
fig.add_subplot(1, 2, 1)

plt.imshow(mat)
plt.title('original')
# plt.gray()

fig.add_subplot(1, 2, 2)

plt.imshow(out)
plt.title('result')
# plt.gray()

plt.show()