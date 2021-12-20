import compress_json
import cv2


imagepath = input("Path to the levelpic: ")

image = cv2.imread(imagepath)
print(len(image), len(image[0]), len(image[0][0]))
matrix = []
for i in range(len(image)):
    matrix.append([])
    for j in range(len(image[0])):
        matrix[i].append([])
        if sum(image[i][j]) == 0:
            matrix[i][j] = "Wall"
        # Needs to be int of colorvalue because else it creates an overflow encounter in ubyte_scalars
        if image[i][j][0] == 255 and int(image[i][j][1]) + int(image[i][j][2]) == 0:
            matrix[i][j] = "Obstacle"

compress_json.dump(matrix, f"{imagepath}.json.bz")  # for a bz2 file
