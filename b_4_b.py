from matplotlib import pyplot as plt
import numpy as np


mat = np.loadtxt('1_3.asc', skiprows=6) # skiprows=6
res = mat / 4

fig = plt.figure(figsize=(10, 7)) #create figure
fig.add_subplot(1, 2, 1)

plt.imshow(mat)
plt.title('original')

fig.add_subplot(1, 2, 2)
plt.imshow(res)
plt.title('result')


# plt.gray()
plt.show()

