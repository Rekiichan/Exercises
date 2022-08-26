from matplotlib import pyplot as plt
import numpy as np

def process(mat):
    rows = len(mat)
    cols = len(mat[0])
    res = np.zeros((int(rows / 4), int(cols / 4)))
    print(res.shape)
    print(mat.shape)
    for row in range(0,rows,4):
        for col in range(0,cols,4):
            average_matrix = mat[row : row + 4, col : col + 4]
            ave = np.average(average_matrix)
            r, c = int(row/4), int(col/4)
            res[r][c] = ave
    return res

if __name__ == "__main__":
    Init_Image = np.loadtxt('1_3.asc')
    Converted_Image = process(Init_Image)

    fig = plt.figure(figsize=(10, 7)) #create figure
    fig.add_subplot(1, 2, 1)

    plt.imshow(Init_Image)
    plt.title('original')

    fig.add_subplot(1, 2, 2)

    plt.imshow(Converted_Image)
    plt.title('result')

    plt.show()

