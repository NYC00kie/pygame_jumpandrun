import cv2
import json

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
        if image[i][j][0] == 255 and image[i][j][1] + image[i][j][2] == 0:
            matrix[i][j] = "Obstacle"

print(matrix)
json_object = json.dumps(matrix, indent=4)

with open(f"{imagepath}.json", "w") as outfile:
    outfile.write(json_object)
