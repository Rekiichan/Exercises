from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def reduceResolution(mat):
    out = cv.resize(src=mat, dsize=(64, 96))
    return out

if __name__ == "__main__":
    matrix = np.loadtxt('1_3.asc')
    res = np.copy(matrix)
    Y1 = reduceResolution(matrix)
    for row in range(0, 96):
        for col in range(0, 64):
            for i in range(0,4):
                for j in range(0,4):
                    res[row*4+i][col*4+j] = int(Y1[row, col])
    
    print(Y1.shape)
    print(res.shape)

    fig = plt.figure(figsize=(10, 7))  # create figure

    fig.add_subplot(1, 2, 1)
    plt.imshow(Y1)
    plt.title('Y1')

    fig.add_subplot(1, 2, 2)
    plt.imshow(res)
    plt.title('result')

    plt.show()
