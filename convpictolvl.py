import compress_json
import cv2
import matplotlib.pyplot as plt
import numpy as np


imagepath = input("Path to the levelpic: ")
iamgename = imagepath.split("/")[-1]
image = cv2.imread(imagepath)
matrix2 = cv2.imread(imagepath)
print(len(image), len(image[0]), len(image[0][0]))
matrix = []

for i in range(len(image)):
    matrix.append([])
    for j in range(len(image[0])):
        matrix[i].append([])
        if sum(image[i][j]) == 0:
            matrix[i][j] = "Wall"
            matrix2[i][j] = (0, 0, 0)
        # Needs to be int of colorvalue because else it creates an overflow encounter in ubyte_scalars
        if image[i][j][0] == 255 and int(image[i][j][1]) + int(image[i][j][2]) == 0:
            matrix[i][j] = "Obstacle"

compress_json.dump(matrix, f"Levels/{iamgename}.json.bz")  # for a bz2 file


cv2.imshow("lele", matrix2)

cv2.waitKey(0)

cv2.destroyAllWindows()
