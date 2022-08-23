from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def process(mat):
    out = cv.resize(src=mat, dsize=(64, 96))
    return out

if __name__ == "__main__":
    mat = np.loadtxt('1_3.asc')
    res = process(mat)

    fig = plt.figure(figsize=(10, 7)) #create figure

    fig.add_subplot(1, 2, 1)
    plt.imshow(mat)
    plt.title('original')

    fig.add_subplot(1, 2, 2)
    plt.imshow(res)
    plt.title('result')

    plt.show()
