import numpy as np
from matplotlib import pyplot as plt

mat = np.loadtxt('1_3.asc')

fig = plt.figure(figsize=(12, 8)) #create figure
fig.add_subplot(2, 2, 1)
plt.gray()
plt.axis("off")
plt.imshow(mat)
plt.title('8 bits')

scale = pow(2,8) / pow(2,6)
out6 = mat / scale
out6 = np.floor(out6)
out6 = out6*scale + scale/2  
fig.add_subplot(2, 2, 2)
plt.axis("off")
plt.imshow(out6)
plt.title('6 bits')

scale = pow(2,8) / pow(2,3)
out3 = mat / scale
out3 = np.floor(out3)
out3 = out3*scale + scale/2
fig.add_subplot(2, 2, 4)
plt.axis("off")
plt.imshow(out3)
plt.title('3 bits')

plt.show()

