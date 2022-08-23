import numpy as np
from matplotlib import pyplot as plt

mat = np.loadtxt('1_3.asc')

fig = plt.figure(figsize=(12, 8)) #create figure
fig.add_subplot(2, 2, 1)

plt.imshow(mat)
plt.title('8 bits')

output6 = mat * 64 / 255 
output6 = np.round_(output6)

fig.add_subplot(2, 2, 2)
plt.imshow(output6)
plt.title('6 bits')

output3 = mat * 8 / 255
output3 = np.round_(output3)

fig.add_subplot(2, 2, 4)
plt.imshow(output3)
plt.title('3 bits')

plt.show()
