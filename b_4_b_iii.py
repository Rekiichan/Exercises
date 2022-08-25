from matplotlib import pyplot as plt
import numpy as np

def reduceResolution(mat):
    matrix = np.loadtxt('1_3.asc')
    res = np.copy(matrix)
    out = cv.resize(src=mat, dsize=(64, 96))
    for row in range(0, 96):
        for col in range(0, 64):
            for i in range(0,4):
                for j in range(0,4):
                    res[row*4+i][col*4+j] = int(Y1[row, col])


if __name__ == "__main__":
    matrix = np.loadtxt('1_3.asc')
    res = np.copy(matrix)
    Y1 = reduceResolution(matrix)
    for row in range(0, 96):
        for col in range(0, 64):
            for i in range(0,4):
                for j in range(0,4):
                    res[row*4+i][col*4+j] = int(Y1[row, col])








def process(mat):
    rows = 384*4
    cols = 256*4
    res = np.random.randn(rows, cols)
    for row in range(0, 383):
        for col in range(0, 255):
            newRow = row*4
            newCol = col*4
            res[newRow][newCol] = mat[row][col]

            val_col = (mat[row][col+1] - mat[row][col]) / 4
            val_row = (mat[row+1][col] - mat[row][col]) / 4

            for i in range(1, 4):
                for j in range(1,4):
                    res[newRow + i][newCol] = val_row*i + mat[row][col]
                    res[newRow][newCol + j] = val_col*j + mat[row][col]
    return res

if __name__ == "__main__":
    matrix = np.loadtxt('1_3.asc')
    res = process(matrix)

    fig = plt.figure(figsize=(12, 9))

    fig.add_subplot(1, 2, 1)
    plt.imshow(matrix)
    plt.title('original')

    fig.add_subplot(1, 2, 2)
    plt.imshow(res)
    plt.title('result')

    plt.show()
