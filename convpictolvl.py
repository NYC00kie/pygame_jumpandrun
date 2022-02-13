import compress_json
import cv2


imagepath = input("Path to the levelpic: ")
iamgenameandextension = imagepath.split("/")[-1]
imagename = iamgenameandextension.split(".")[0]
image = cv2.imread(imagepath)
print(len(image), len(image[0]), len(image[0][0]))
matrix = []
# y Axis
for i in range(len(image)):
    matrix.append([])
    # x Axis
    for j in range(len(image[0])):
        matrix[i].append([])
        # colors are formated in  BGR (Blue Green Red)
        # Needs to be int of colorvalue because else it creates an overflow encounter in ubyte_scalars
        if sum(image[i][j]) == 0:
            matrix[i][j] = "Wall"

        if int(image[i][j][0]) == 255 and int(image[i][j][1]) + int(image[i][j][2]) == 0:
            matrix[i][j] = "Obstacle"

        if int(image[i][j][0]) == 17 and int(image[i][j][1]) == 160 and int(image[i][j][2]) == 33:
            matrix[i][j] = "PSpawn"
            print("Spawn")

        if int(image[i][j][1]) + int(image[i][j][0]) == 0 and int(image[i][j][2]) == 255:
            matrix[i][j] = "PFinish"
            print("Finish")

        if int(image[i][j][0]) == 0 and int(image[i][j][1]) == 255 and int(image[i][j][2]) == 255:
            matrix[i][j] = "Coin"
            print("Coin")


# for a bz2 file
compress_json.dump(matrix, f"Levels/{imagename}.json.bz")
