from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def b1():
    Init_Image = np.loadtxt('1_3.asc')
    Enlarged_Image = np.zeros((384,256))
    reduced_resolution_image = cv.resize(src=Init_Image, dsize=(64, 96))
    for row in range(0, 96):
        for col in range(0, 64):
            for i in range(0,4):
                for j in range(0,4):
                    Enlarged_Image[row*4+i][col*4+j] = int(reduced_resolution_image[row, col])
    return Enlarged_Image

def b2():
    Init_Image = np.loadtxt('1_3.asc')
    rows = len(Init_Image) * 4
    cols = len(Init_Image[0]) * 4
    convertedImage = np.zeros((rows,cols))
    for row in range(0, len(Init_Image) - 1):
        for col in range(0, len(Init_Image[0]) - 1):
            newRow, newCol = row*4, col*4
            convertedImage[newRow][newCol] = Init_Image[row][col]
            val_col = (Init_Image[row][col+1] - Init_Image[row][col]) / 4
            val_row = (Init_Image[row+1][col] - Init_Image[row][col]) / 4
            for i in range(1, 4):
                for j in range(1,4):
                    convertedImage[newRow + i][newCol] = val_row*i + Init_Image[row][col]
                    convertedImage[newRow][newCol + j] = val_col*j + Init_Image[row][col]
    return convertedImage

if __name__ == "__main__":
    B1_image = b1()
    B2_image = b2()

    fig = plt.figure(figsize=(12, 9))

    fig.add_subplot(1, 2, 1)
    plt.imshow(B1_image)
    plt.title('B1_image')

    fig.add_subplot(1, 2, 2)
    plt.imshow(B2_image)
    plt.title('B2_image')

    plt.show()
