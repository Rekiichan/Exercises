from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def Reduce_Resolution(mat, factorValue):
    cols = int(len(mat[0]) / factorValue)
    rows = int(len(mat) / factorValue)
    out = cv.resize(src=mat, dsize=(cols,rows))
    return out

def b1(Init_Image,factorValue):
    r, c = Init_Image.shape
    Enlarged_Image = np.zeros((r,c))
    reduced_resolution_image = Reduce_Resolution(Init_Image, factorValue)
    rows, cols = int(r/4), int(c/4)
    for row in range(0, rows):
        for col in range(0, cols):
            Enlarged_Image[row*4:row*4+4,col*4:col*4+4] = reduced_resolution_image[row, col]
    return Enlarged_Image

def b2(Init_Image,factorValue):
    Enlarged_Image = np.zeros((384,256))
    Reduced_Image = Reduce_Resolution(Init_Image, 4)
    rowReduImg = len(Reduced_Image)
    colReduImg = len(Reduced_Image[0])
    rows = rowReduImg + (factorValue - 1) * (rowReduImg - 1)
    cols = colReduImg + (factorValue - 1) * (colReduImg- 1)

    Enlarged_Image = np.zeros((rows,cols))

    for row in range(0,rows,factorValue):
        for col in range(0,cols,factorValue):
            Enlarged_Image[row][col] = Reduced_Image[int(row/factorValue)][int(col/factorValue)]

    for row in range(0,rows,factorValue):
        for col in range(1, cols,factorValue):
            value = Enlarged_Image[row][col + factorValue - 1] - Enlarged_Image[row][col - 1]
            value = value / factorValue
            for i in range(col,factorValue + col - 1):
                Enlarged_Image[row][i] = Enlarged_Image[row][col - 1] + value*(i%factorValue)

    for col in range(0,cols):
        for row in range(1, rows,factorValue):
            value = Enlarged_Image[row + factorValue - 1][col] - Enlarged_Image[row - 1][col]
            value = value / factorValue
            for i in range(row,factorValue + row - 1):
                Enlarged_Image[i][col] = Enlarged_Image[row - 1][col] + value*(i%factorValue)  
    return Enlarged_Image

if __name__ == "__main__":
    Init_Image = np.loadtxt('1_3.asc')
    B1_image = b1(Init_Image,4)
    B2_image = b2(Init_Image,4)

    fig = plt.figure(figsize=(12, 9))
    plt.gray()
    fig.add_subplot(1, 2, 1)
    plt.imshow(B1_image)
    plt.title('B1_image')

    fig.add_subplot(1, 2, 2)
    plt.imshow(B2_image)
    plt.title('B2_image')

    plt.show()

