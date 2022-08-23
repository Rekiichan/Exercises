import cv2 as cv

def process(src):
    img = cv.imread(src)
    res = cv.imread(src) 
    for row in range(0,4):
        for col in range(0,4):
            rev_row = 3 - row
            rev_col = 3 - col
            for index_row in range(0,32):
                for index_col in range(0,32):
                    res[rev_row*32 + index_row][rev_col*32 + index_col] = img[row*32 + index_row][col*32 + index_col]
            
    cv.imshow('original img', img)
    cv.imshow('converted img', res)
    cv.waitKey()
    cv.destroyAllWindows()

if __name__ == "__main__":
    process('1_2.tif')