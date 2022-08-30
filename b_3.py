import cv2 as cv

def process(src, rowsOfBlock, colsOfBlock):
    img = cv.imread(src)
    out = cv.imread(src)
    rows = len(img)
    cols = len(img[0])
    rowOfOneBlock = int(rows / rowsOfBlock)
    colOfOneBlock = int(cols / colsOfBlock)

    for row in range(0,rowsOfBlock):
        for col in range(0,colsOfBlock):
            rev_row = rowsOfBlock - 1 - row
            rev_col = colsOfBlock - 1 - col
            for index_row in range(0,rowOfOneBlock):
                for index_col in range(0,colOfOneBlock):
                    out[rev_row*rowOfOneBlock + index_row][rev_col*colOfOneBlock + index_col] = img[row*rowOfOneBlock + index_row][col*colOfOneBlock + index_col]
    return img, out

if __name__ == "__main__":
    img, out = process('1_2.tif',4,4)

    cv.imshow('original img', img)
    cv.imshow('converted img', out)
    cv.waitKey()
    cv.destroyAllWindows()


    