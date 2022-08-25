from matplotlib import pyplot as plt
import numpy as np

def Bilinear_Interpolation(mat, factorValue):

    # lay so hang va so cot de khoi tao ma tran ket qua 
    rows = len(mat) * factorValue
    cols = len(mat[0]) * factorValue

    #khoi tao ma tran ket qua
    convertedImage = np.zeros((rows, cols))
    
    for row in range(0, len(mat) - 1):
        for col in range(0, len(mat[0]) - 1):

            #newRow va newCol lan luot la so hang va so cot cua ma tran sau khi converted
            newRow, newCol = row*factorValue, col*factorValue
            convertedImage[newRow][newCol] = mat[row][col]

            # Tinh gia tri giua cac diem pivot
            val_col = (mat[row][col+1] - mat[row][col]) / factorValue
            val_row = (mat[row+1][col] - mat[row][col]) / factorValue

            for i in range(1, factorValue):
                for j in range(1,factorValue):
                    convertedImage[newRow + i][newCol] = val_row*i + mat[row][col]
                    convertedImage[newRow][newCol + j] = val_col*j + mat[row][col]
    return convertedImage

if __name__ == "__main__":
    matrix = np.loadtxt('1_3.asc')
    res = Bilinear_Interpolation(matrix, 4)

    fig = plt.figure(figsize=(12, 9))

    fig.add_subplot(1, 2, 1)
    plt.imshow(matrix)
    plt.title('original')

    fig.add_subplot(1, 2, 2)
    plt.imshow(res)
    plt.title('result')

    plt.show()
