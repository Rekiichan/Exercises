from matplotlib import pyplot as plt
import numpy as np
from PIL import Image as im










mat = np.loadtxt('1_3.asc') # skiprows=6
image = mat.resize(400,400)


# res = np.copy(mat)
# rows = len(mat)
# cols = len(mat[0])
# factorCols = round((cols/4), -1)
# factorRows = round((rows/4), -1)
# factorCols = int(factorCols)
# factorRows = int(factorRows)
# res.resize(factorRows,factorCols)

fig = plt.figure(figsize=(10, 7)) #create figure
fig.add_subplot(1, 2, 1)

plt.imshow(image)
plt.title('original')

# fig.add_subplot(1, 2, 2)
# plt.imshow(res)
# plt.title('result')


plt.gray()
plt.show()

