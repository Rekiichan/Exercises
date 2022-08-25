from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def reduceResolution(mat):
    out = cv.resize(src=mat, dsize=(64, 96))
    return out

if __name__ == "__main__":
    Init_Image = np.loadtxt('1_3.asc')
    print(Init_Image.shape)
    Enlarged_Image = np.zeros((384,256))
    reduced_resolution_image = reduceResolution(Init_Image)
    for row in range(0, 96):
        for col in range(0, 64):
            for i in range(0,4):
                for j in range(0,4):
                    Enlarged_Image[row*4+i][col*4+j] = int(reduced_resolution_image[row, col])

    fig = plt.figure(figsize=(10, 7))  # create figure

    fig.add_subplot(1, 2, 1)
    plt.imshow(reduced_resolution_image)
    plt.title('Reduced Resolution Image')

    fig.add_subplot(1, 2, 2)
    plt.imshow(Enlarged_Image)
    plt.title('Enlarged Image')

    plt.show()
