from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

def Reduce_Resolution(mat, factorValue):
    cols = int(len(mat[0]) / factorValue)
    rows = int(len(mat) / factorValue)
    out = cv.resize(src=mat, dsize=(cols,rows))
    return out

def Bilinear_Interpolation(Reduced_Image,factorValue):
    rowReduImg = len(Reduced_Image)
    colReduImg = len(Reduced_Image[0])
    
    # Get size of converted matrix
    rows = rowReduImg + (factorValue - 1) * (rowReduImg - 1)
    cols = colReduImg + (factorValue - 1) * (colReduImg- 1)
    # Init converted matrix
    convertedImage = np.zeros((rows,cols))
    # Define pivot in converted matrix
    for row in range(0,rows,factorValue):
        for col in range(0,cols,factorValue):
            convertedImage[row][col] = Reduced_Image[int(row/factorValue)][int(col/factorValue)]
    # Scan all row pivot to define pixel
    for row in range(0,rows,factorValue):
        for col in range(1, cols,factorValue):
            value = convertedImage[row][col + factorValue - 1] - convertedImage[row][col - 1]
            value = value / factorValue
            for i in range(col,factorValue + col - 1):
                convertedImage[row][i] = convertedImage[row][col - 1] + value*(i%factorValue)
    # Define all remaining pixels
    for col in range(0,cols):
        for row in range(1, rows,factorValue):
            value = convertedImage[row + factorValue - 1][col] - convertedImage[row - 1][col]
            value = value / factorValue
            for i in range(row,factorValue + row - 1):
                convertedImage[i][col] = convertedImage[row - 1][col] + value*(i%factorValue)  
    return convertedImage

if __name__ == "__main__":
    Init_Image = np.loadtxt('1_3.asc')
    Reduced_Image = Reduce_Resolution(Init_Image,4)
    Enlarged_Image = Bilinear_Interpolation(Reduced_Image,4)
    # np.savetxt('result.asc',Enlarged_Image)

    fig = plt.figure(figsize=(12, 9))
    plt.gray()
    fig.add_subplot(1, 2, 1)
    plt.imshow(Reduced_Image)
    plt.title('Reduced_Image')
    fig.add_subplot(1, 2, 2)
    plt.imshow(Enlarged_Image)
    plt.title('Enlarged_Image')
    plt.show()


    