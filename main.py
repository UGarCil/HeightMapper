# Program created by Uriel Garcilazo Cruz on 6/26/2022. The program consumes an image, reducing its dimensions to squares of 16/16.
# Each square will also map the amount of white/black inside to produce instead a gamma of colors.

# MODULES
import cv2
import numpy as np
import random

# CONSTANTS
IMG_NAME = "victoria"
IMG = cv2.imread(f"{IMG_NAME}.png")
IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
n=2

# DATA DEFINITIONS
# DD. AVERAGEPIXEL
# avgPix = [[i = n], ..., j = n]
# interp. the average value of a grid of nxn pixels in the screen
# Example: n=4
avgPix0 = [[IMG[0][0],IMG[0][1],IMG[0][2],IMG[0][3]],\
           [IMG[1][0],IMG[1][1],IMG[1][2],IMG[1][3]],\
           [IMG[2][0],IMG[2][1],IMG[2][2],IMG[2][3]],\
           [IMG[3][0],IMG[3][1],IMG[3][2],IMG[3][3]]]
avgPix0 = sum([sum(row) for row in avgPix0])/(4*4)

avgPix1 = [[IMG[0][4],IMG[0][5],IMG[0][6],IMG[0][7]],\
           [IMG[1][4],IMG[1][5],IMG[1][6],IMG[1][7]],\
           [IMG[2][4],IMG[2][5],IMG[2][6],IMG[2][7]],\
           [IMG[3][4],IMG[3][5],IMG[3][6],IMG[3][7]]]
avgPix1 = sum([sum(row) for row in avgPix1])/(4*4)




# FD. getAverage()
# Signature: AVERAGEPIXEL -> int
# purp. get the sum of all the values of gray in the pixels included in the 2D array
def getAverageNxN(avgPix):
    return sum([sum(row) for row in avgPix])




# DD. AVGPIXELROW
# avgPixRow = [AVERAGEPIXEL, ...]
# interp. a row of average pixel values for nxn dimensions
avgPixRow0 = [avgPix0, avgPix1]


# DD. GRID
# grid = [AVGPIXELROW, ...]
# interp. a grid of rows of average pixel rows
grid = []

rows = 0
cols = 0
while rows + (n-1) <= IMG.shape[0]:
    cols = 0
    avgPixRow = []
    while cols + (n-1) <= IMG.shape[1]:
        avgPix = getAverageNxN(IMG[rows:rows+(n-1),cols:cols+(n-1)])
        avgPixRow.append(avgPix/(n*n))
        cols += n
        # input()
    grid.append(avgPixRow)
    rows += n

# Getting the maximum value of the array will allow us to scale the new resolution to a range from 0 to 1
MAXVALGRID = np.max(grid)

normalizedGrid = []

for avgPixRow in grid:
    normalized_avgPixRow = []
    for avgPix in avgPixRow:
        normalized_avgPix = avgPix/MAXVALGRID
        normalized_avgPixRow.append(normalized_avgPix)
    normalizedGrid.append(normalized_avgPixRow)





 #    B   ,    G   ,    R
def getRandomColor():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    return([r,g,b])

# DD. RANDOMCOLORS
# randomColors = [[int,int,int], ...,  i=10]
# interp. a list of random colors
randomColors = [getRandomColor() for x in range(10)]


# FD. colorize()
# Signature: AVERAGEPIXEL -> [int, int, int]
# purp. map color based on a threshold that goes from 0.0 to 1:
# [0-0.2, 0.2-0.3, 0.3-0.4, 0.4-0.5, 0.5-0.6, 0.6-0.7, 0.7-0.8, 0.8-0.9, 0.9-1]
def colorize(avgPix):
    if avgPix < 0.1:
        return(randomColors[0])
    if avgPix < 0.2:
        return(randomColors[1])
    if avgPix < 0.3:
        return(randomColors[2])
    if avgPix < 0.4:
        return(randomColors[3])
    if avgPix < 0.5:
        return(randomColors[4])
    if avgPix < 0.6:
        return(randomColors[5])
    if avgPix < 0.7:
        return(randomColors[6])
    if avgPix < 0.8:
        return(randomColors[7])
    if avgPix < 0.9:
        return(randomColors[8])
    else:
        return(randomColors[9])




# Getting the normalized values in the array will allow us to colorize based on different values:

colorizedNormGrid = []
for avgPixRow in normalizedGrid:
    normalized_ColoredavgPixRow = []
    for avgPix in avgPixRow:
        color_avgPix = colorize(avgPix)
        normalized_ColoredavgPixRow.append(color_avgPix)
    colorizedNormGrid.append(normalized_ColoredavgPixRow)









# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
# CODE STARTS BELOW
grid = colorizedNormGrid


# Transform the 2D list into a numpy array to enable cv2 to visualize it
AVGIMG = np.array(grid)
print(AVGIMG.shape)
cv2.imwrite(f"{IMG_NAME}_output.png", AVGIMG)





# while True:
# # AVGIMG = cv2.IMREAD_GRAYSCALE(AVGIMG)
#     cv2.imshow("test",AVGIMG)
#     if cv2.waitKey(1) & 0xFF == ord ("q"):
#         break
#     # cap1.release()
#     ##out.release()
# cv2.destroyAllWindows() 