from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def process(mat, factorValue):
    cols = int(len(mat[0]) / factorValue)
    rows = int(len(mat) / factorValue)
    out = cv.resize(src=mat, dsize=(cols,rows))
    return out

if __name__ == "__main__":
    Init_Image = np.loadtxt('1_3.asc')
    reduced_image = process(Init_Image,4)
    fig = plt.figure(figsize=(10, 7)) #create figure
    plt.gray()
    fig.add_subplot(1, 2, 1)
    
    plt.imshow(Init_Image)
    plt.title('original')

    fig.add_subplot(1, 2, 2)
    plt.imshow(reduced_image)
    plt.title('result')

    plt.show()

