from matplotlib import pyplot as plt
import numpy as np

def process(mat):
    res = np.zeros((96, 64))
    rows = len(mat)     #384 / 4 = 96
    cols = len(mat[0])  #256 / 4 = 64

    for row in range(0,rows,4):
        for col in range(0,cols,4):
            sum = 0
            for i in range(row, row + 4):
                for j in range(col, col + 4):
                    sum += mat[i][j]

            r, c = int(row/4), int(col/4)
            res[r][c] = int(sum/16)

    return res

if __name__ == "__main__":
    mat = np.loadtxt('1_3.asc') # skiprows=6
    res = process(mat)

    fig = plt.figure(figsize=(10, 7)) #create figure
    fig.add_subplot(1, 2, 1)

    plt.imshow(mat)
    plt.title('original')

    fig.add_subplot(1, 2, 2)

    plt.imshow(res)
    plt.title('result')

    plt.show()